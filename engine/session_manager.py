"""
Session Persistence Module
Saves and loads practice session state to/from JSON files.
"""
import os
import json
import datetime


class SessionManager:
    """Manages saving and loading IELTS practice session state."""
    
    def __init__(self, data_dir=None):
        if data_dir is None:
            data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sessions")
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
    
    def get_session_path(self, book, test_name):
        """Get path for session JSON file."""
        safe_name = f"{book}_{test_name}".replace(" ", "_")
        return os.path.join(self.data_dir, f"{safe_name}.json")
    
    def save_session(self, book, test_name, part_name, question_index, 
                     conversation_history, attempts_count, streak_data=None):
        """Save current session state."""
        path = self.get_session_path(book, test_name)
        session = {
            "book": book,
            "test": test_name,
            "part": part_name,
            "question_index": question_index,
            "conversation_history": conversation_history,
            "attempts_count": attempts_count,
            "streak_data": streak_data or {},
            "last_updated": datetime.datetime.now().isoformat()
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(session, f, ensure_ascii=False, indent=2)
        return path
    
    def load_session(self, book, test_name):
        """Load saved session state."""
        path = self.get_session_path(book, test_name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    
    def delete_session(self, book, test_name):
        """Delete saved session."""
        path = self.get_session_path(book, test_name)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False
    
    def get_all_sessions(self):
        """List all saved sessions."""
        sessions = []
        if not os.path.exists(self.data_dir):
            return sessions
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".json"):
                path = os.path.join(self.data_dir, fname)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        sessions.append({
                            "book": data.get("book", "Unknown"),
                            "test": data.get("test", "Unknown"),
                            "part": data.get("part", "Unknown"),
                            "last_updated": data.get("last_updated", ""),
                            "path": path
                        })
                except:
                    pass
        return sessions
    
    def save_completed_test(self, book, test_name, results):
        """Save completed test results."""
        path = os.path.join(self.data_dir, "completed", f"{book}_{test_name}.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        data = {
            "book": book,
            "test": test_name,
            "results": results,
            "completed_at": datetime.datetime.now().isoformat()
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path
    
    def get_unsatisfactory_sessions(self):
        """Get sessions where Eric did not meet standard."""
        unsatisfactory = []
        for session in self.get_all_sessions():
            session_path = session["path"]
            with open(session_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data.get("streak_data", {}).get("below_standard"):
                unsatisfactory.append(data)
        return unsatisfactory
