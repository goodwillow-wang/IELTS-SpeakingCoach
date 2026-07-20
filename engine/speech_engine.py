"""
Speech Engine Module
Uses Windows SAPI for Text-to-Speech and Dictation Recognition
"""
import win32com.client
import pythoncom
import threading
import time
import queue
import wave


class SpeechEngine:
    """Handles TTS (speaking) and Dictation (listening) via Windows SAPI."""
    
    def __init__(self):
        self._tts_lock = threading.Lock()
        self._stop_listen = threading.Event()
    
    def _ensure_com(self):
        try:
            pythoncom.CoInitialize()
        except:
            pass
    
    def speak(self, text, rate=0):
        with self._tts_lock:
            self._ensure_com()
            try:
                voice = win32com.client.Dispatch("SAPI.SpVoice")
                voices = voice.GetVoices()
                for i in range(voices.Count):
                    desc = voices.Item(i).GetDescription()
                    if "Zira" in desc or "David" in desc:
                        voice.Voice = voices.Item(i)
                        break
                voice.Rate = rate
                voice.Volume = 100
                voice.Speak(text, 0)
            except Exception as e:
                print(f"TTS Error: {e}")
    
    def speak_async(self, text, rate=0, callback=None):
        def _speak():
            self.speak(text, rate)
            if callback:
                callback()
        t = threading.Thread(target=_speak, daemon=True)
        t.start()
        return t
    
    def listen_dictation(self, timeout=30):
        self._ensure_com()
        result_queue = queue.Queue()
        
        class RecoEvents:
            def OnRecognition(self, streamNumber, streamPosition, recognitionType, result):
                try:
                    phrase = result.PhraseInfo.GetText()
                    if phrase and phrase.strip():
                        result_queue.put(phrase.strip())
                except:
                    pass
        
        try:
            recognizer = win32com.client.Dispatch("SAPI.SpInprocRecognizer")
            reco_context = recognizer.CreateRecoContext()
            events = RecoEvents()
            reco_context.RecoEvents = events
            grammar = reco_context.CreateGrammar(0)
            try:
                grammar.SetDictationState(1)
            except:
                pass
            
            start = time.time()
            result = ""
            while time.time() - start < timeout:
                pythoncom.PumpWaitingMessages()
                try:
                    result = result_queue.get_nowait()
                    if result:
                        break
                except queue.Empty:
                    pass
                time.sleep(0.05)
            
            try:
                grammar.SetDictationState(0)
            except:
                pass
            return result
        except:
            return ""
    
    def stop_listening(self):
        self._stop_listen.set()
    
    def get_audio_devices(self):
        devices = []
        try:
            import sounddevice as sd
            for i, d in enumerate(sd.query_devices()):
                devices.append({
                    "index": i, "name": d["name"],
                    "channels": d["max_input_channels"],
                    "default_samplerate": d["default_samplerate"]
                })
        except:
            devices.append({"index": 0, "name": "System Default"})
        return devices
    
    def record_audio(self, duration=10, samplerate=16000):
        try:
            import sounddevice as sd
            import numpy as np
            recording = sd.rec(int(duration * samplerate), samplerate=samplerate,
                              channels=1, dtype="int16")
            sd.wait()
            return recording.flatten()
        except:
            return None
    
    def save_audio_to_wav(self, audio_data, filepath, samplerate=16000):
        import numpy as np
        with wave.open(filepath, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(samplerate)
            wf.writeframes(audio_data.tobytes())
        return filepath