"""
IELTS Speaking Scoring Engine
Evaluates responses based on IELTS 7 band criteria:
- Fluency & Coherence
- Lexical Resource (Vocabulary)
- Grammatical Range & Accuracy
- Pronunciation
- Task Achievement
"""
import re
import time
import math


class IELTSScorer:
    """Evaluates speaking responses against IELTS 7 band criteria."""
    
    def __init__(self):
        self.band_descriptors = {
            "fluency_coherence": {
                9: "Fluent with only very occasional repetition. Sustained use of accurate language. Hesitation only to prepare content.",
                8: "Fluent with only very occasional repetition. Hesitation occasionally for content. Topic development coherent and relevant.",
                7: "Keeps going and readily produces long turns. Uses a range of connectives. Some hesitation, repetition or self-correction.",
                6: "Willing to speak at length, though coherence may be lost at times. Uses discourse markers not always appropriately.",
                5: "Usually able to keep going, but relies on repetition/self-correction. Hesitations for basic lexis and grammar.",
                4: "Cannot respond without noticeable pauses. Only simple speech, frequently with repetition and hesitation.",
                3: "Frequent long pauses while searching for words. Limited ability to link sentences.",
                2: "Lengthy pauses before nearly every word. Virtually no communicative significance.",
                1: "Essentially no rateable language. Speech is totally incoherent."
            },
            "lexical_resource": {
                9: "Total flexibility and precise use in all contexts. Skilful use of idiomatic language naturally.",
                8: "Wide resource, readily and flexibly used. Skilful use of less common items despite occasional inaccuracies.",
                7: "Resource sufficient to discuss topics at length. Good paraphrasing. Uses some less common vocabulary.",
                6: "Resource sufficient for topics at some length. Generally able to paraphrase. Some inappropriacies in word choice.",
                5: "Resource sufficient for familiar topics but limited flexibility. Attempts paraphrase not always successful.",
                4: "Limited vocabulary, primarily basic. Inadequate for unfamiliar topics. Frequent word choice errors.",
                3: "Limited to simple vocabulary for personal information. Frequently unable to convey basic meaning.",
                2: "Very limited resource. Utterances are isolated words or memorised utterances.",
                1: "No resource bar a few isolated words. No communication possible."
            },
            "grammatical_range": {
                9: "Structures are precise and accurate at all times. Full range of structures used naturally.",
                8: "Wide range of structures, flexibly used. Majority of sentences error-free. Occasional non-systematic errors.",
                7: "Mix of short and complex sentence forms. Frequent error-free sentences. Good grammatical control.",
                6: "Mix of short and complex forms with limited flexibility. Errors in complex structures but rarely impede.",
                5: "Basic sentence forms fairly well controlled. Complex structures limited and nearly always contain errors.",
                4: "Basic forms attempted but numerous errors except in memorised utterances.",
                3: "No evidence of basic sentence forms except memorised. Numerous grammatical errors.",
                2: "No evidence of basic sentence forms. Delivery problems impair connected speech.",
                1: "No rateable language unless memorised."
            },
            "pronunciation": {
                9: "Full range of phonological features for precise meaning. Flexible connected speech. Effortlessly understood.",
                8: "Wide range of phonological features. Appropriate rhythm. Flexible stress/intonation. Easily understood.",
                7: "Range of phonological features, control variable. Chunking generally appropriate. Some effective intonation/stress.",
                6: "Range of features but not sustained. Chunking appropriate. Some effective intonation but limited.",
                5: "Some features of band 4 and some of band 6. Occasional mispronunciation but meaning usually clear.",
                4: "Few acceptable phonological features. Isolated words may be recognisable.",
                3: "Individual words and phonemes mainly mispronounced. Little meaning conveyed.",
                2: "Often unintelligible. Little meaning conveyed.",
                1: "Can produce occasional recognisable words but no overall meaning. Unintelligible."
            },
            "task_achievement": {
                9: "Fully addresses all parts with well-developed, relevant and extended responses.",
                8: "Addresses all parts with well-developed responses and relevant detail throughout.",
                7: "Addresses all parts of the task. Well-developed responses with relevant supporting detail.",
                6: "Addresses all parts though some may be more fully covered. Relevant but may lack detail.",
                5: "Addresses task only partially. Mainly relevant but may lack specific detail.",
                4: "Attempts task but does not address all parts. May be off-topic at times.",
                3: "Addresses task only minimally. Frequently off-topic. Very limited content.",
                2: "Hardly addresses the task. Mostly irrelevant or very brief.",
                1: "Does not address the task. Completely unrelated or insufficient."
            }
        }
    
    def estimate_word_count(self, text):
        """Count words in the response."""
        words = text.strip().split()
        return len(words)
    
    def estimate_speaking_duration(self, text, words_per_minute=140):
        """Estimate how long it would take to speak this text."""
        word_count = self.estimate_word_count(text)
        return word_count / words_per_minute * 60  # in seconds
    
    def analyze_fluency(self, text):
        """Analyze fluency and coherence."""
        score = 5  # default
        details = []
        
        word_count = self.estimate_word_count(text)
        
        # Check for connectives
        connectives = [
            "first", "second", "third", "finally", "moreover", "furthermore",
            "however", "therefore", "consequently", "in addition", "on the other hand",
            "in conclusion", "for example", "for instance", "in particular",
            "as a result", "because", "although", "while", "despite",
            "not only", "as well as", "additionally", "specifically"
        ]
        
        found_connectives = []
        for c in connectives:
            if re.search(r'\b' + re.escape(c) + r'\b', text.lower()):
                found_connectives.append(c)
        
        connective_count = len(found_connectives)
        
        # Longer text with more connectives = better fluency
        if word_count >= 100 and connective_count >= 4:
            score = 7
            details.append(f"Good length ({word_count} words) with {connective_count} connectives")
        elif word_count >= 60 and connective_count >= 2:
            score = 6
            details.append(f"Adequate length ({word_count} words) with {connective_count} connectives")
        elif word_count >= 30:
            score = 5
            details.append(f"Short response ({word_count} words)")
        else:
            score = 4
            details.append(f"Very short response ({word_count} words)")
        
        # Check for hesitation markers
        hesitation = ["um", "uh", "er", "ah", "like", "you know"]
        hesitation_count = sum(1 for h in hesitation if re.search(r'\b' + re.escape(h) + r'\b', text.lower()))
        
        if hesitation_count > 3:
            details.append(f"Some hesitation ({hesitation_count} fillers)")
            score = max(score - 1, 4)
        
        return {
            "score": score,
            "word_count": word_count,
            "connectives_found": found_connectives,
            "connective_count": connective_count,
            "details": "; ".join(details)
        }
    
    def analyze_vocabulary(self, text):
        """Analyze lexical resource."""
        score = 5
        details = []
        
        word_count = self.estimate_word_count(text)
        if word_count == 0:
            return {"score": 1, "details": "No response to analyze"}
        
        unique_words = set(w.lower().strip(".,!?;:'\"()[]") for w in text.split())
        unique_count = len(unique_words)
        
        # Check for less common / academic vocabulary
        advanced_words = [
            "significant", "essential", "crucial", "beneficial", "substantial",
            "phenomenon", "perspective", "fundamental", "inevitable", "consequently",
            "nevertheless", "alternatively", "comprehensive", "effectively", "explicitly",
            "considerable", "remarkable", "prevalent", "inevitable", "ultimately",
            "demonstrate", "illustrate", "indicate", "contribute", "facilitate",
            "opportunity", "challenge", "experience", "situation", "development",
            "individual", "society", "environment", "community", "technology",
            "education", "communication", "relationship", "achievement", "influence"
        ]
        
        advanced_used = [w for w in advanced_words if w in unique_words]
        
        if unique_count >= 50 and len(advanced_used) >= 4:
            score = 7
            details.append(f"Good vocabulary range ({unique_count} unique, {len(advanced_used)} advanced)")
        elif unique_count >= 30 and len(advanced_used) >= 2:
            score = 6
            details.append(f"Adequate vocabulary ({unique_count} unique, {len(advanced_used)} advanced)")
        elif unique_count >= 15:
            score = 5
            details.append(f"Limited vocabulary ({unique_count} unique)")
        else:
            score = 4
            details.append(f"Very limited vocabulary")
        
        # Check for paraphrasing (repetition of root words)
        repeated_words = {}
        for w in text.lower().split():
            w_clean = w.strip(".,!?;:'\"()[]")
            if len(w_clean) > 3:
                repeated_words[w_clean] = repeated_words.get(w_clean, 0) + 1
        
        excessive_repeat = [w for w, c in repeated_words.items() if c > 3]
        if len(excessive_repeat) > 3:
            details.append(f"Some word repetition")
            score = max(score - 1, 4)
        
        return {
            "score": score,
            "unique_words": unique_count,
            "advanced_words": advanced_used,
            "details": "; ".join(details)
        }
    
    def analyze_grammar(self, text):
        """Analyze grammatical range and accuracy."""
        score = 5
        details = []
        
        if not text.strip():
            return {"score": 1, "details": "No response"}
        
        # Simple sentence detection
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)
        
        # Count complex sentence markers (subordinate clauses)
        complex_markers = ["because", "although", "while", "since", "unless",
                          "when", "which", "that", "where", "who", "whom",
                          "whose", "if", "whether", "despite", "in spite of"]
        
        complex_count = 0
        for s in sentences:
            for m in complex_markers:
                if re.search(r'\b' + re.escape(m) + r'\b', s.lower()):
                    complex_count += 1
                    break
        
        complex_ratio = complex_count / max(sentence_count, 1)
        
        # Check tenses variety
        tense_markers = {
            "past": ["was", "were", "did", "had", "went", "saw", "made", "told",
                     "played", "worked", "studied", "lived", "visited", "liked"],
            "present": ["is", "are", "do", "does", "have", "has", "go", "make",
                       "play", "work", "study", "live", "like"],
            "future": ["will", "shall", "going to", "would", "plan to", "hope to"]
        }
        
        tense_usage = {}
        for tense, words in tense_markers.items():
            used = [w for w in words if re.search(r'\b' + re.escape(w) + r'\b', text.lower())]
            if used:
                tense_usage[tense] = len(used)
        
        tense_count = len(tense_usage)
        
        # Scoring
        if sentence_count >= 5 and complex_ratio >= 0.4 and tense_count >= 2:
            score = 7
            details.append(f"Complex structures ({complex_count}/{sentence_count}={complex_ratio:.0%})")
        elif sentence_count >= 3 and complex_ratio >= 0.2 and tense_count >= 1:
            score = 6
            details.append(f"Mix of simple and complex ({complex_count}/{sentence_count})")
        elif sentence_count >= 2:
            score = 5
            details.append("Mostly simple sentences")
        else:
            score = 4
            details.append("Very limited sentence structure")
        
        if tense_count >= 2:
            details.append(f"Good tense variety ({tense_count} tenses)")
        
        return {
            "score": score,
            "sentence_count": sentence_count,
            "complex_ratio": complex_ratio,
            "tense_count": tense_count,
            "details": "; ".join(details)
        }
    
    def analyze_pronunciation(self, text):
        """Analyze pronunciation readiness based on text.
        In a real app, this would use audio analysis.
        Here we check for indicators of phonological awareness."""
        score = 5
        details = []
        
        if not text.strip():
            return {"score": 1, "details": "No response"}
        
        # Check for varied sentence lengths (indicates prosody awareness)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if sentences:
            lengths = [len(s.split()) for s in sentences]
            avg_len = sum(lengths) / len(lengths)
            length_variety = max(lengths) - min(lengths) if len(lengths) > 1 else 0
            
            if avg_len > 12 and length_variety > 5:
                score = 7
                details.append("Good sentence length variety (indicates prosody)")
            elif avg_len > 8 and length_variety > 3:
                score = 6
                details.append("Adequate sentence length variety")
            else:
                details.append("Limited sentence variety")
        
        # Check for contractions (natural speech indicator)
        contractions = ["I'm", "I've", "I'll", "I'd", "don't", "doesn't", "didn't",
                       "can't", "won't", "wouldn't", "couldn't", "it's", "that's",
                       "there's", "they're", "we're", "we'll", "we've", "they've",
                       "you're", "you'll", "you've"]
        contraction_count = sum(1 for c in contractions if c.lower() in text.lower())
        
        if contraction_count >= 3:
            details.append(f"Natural speech markers ({contraction_count} contractions)")
            score = min(score + 1, 7)
        
        return {
            "score": score,
            "avg_sentence_length": round(avg_len, 1) if sentences else 0,
            "contraction_count": contraction_count,
            "details": "; ".join(details)
        }
    
    def analyze_task_achievement(self, text, question_info):
        """Analyze how well the task was addressed.
        question_info should include prompts from the cue card or part questions."""
        score = 5
        details = []
        
        if not text.strip():
            return {"score": 1, "details": "No response"}
        
        word_count = self.estimate_word_count(text)
        
        if isinstance(question_info, list):
            # Part 1 or Part 3: list of questions
            # Check response addresses key themes
            for q in question_info:
                keywords = re.findall(r'\b\w+\b', q.lower())
                keywords = [k for k in keywords if len(k) > 3]
                for k in keywords[:5]:
                    if k in text.lower():
                        details.append(f"Mentions: {k}")
                        break
            
            if word_count >= 40:
                score = 7
                details.append(f"Good response length for interview question ({word_count} words)")
            elif word_count >= 20:
                score = 6
                details.append(f"Adequate response ({word_count} words)")
            else:
                score = 5
                details.append(f"Brief response ({word_count} words)")
        
        elif isinstance(question_info, dict):
            # Part 2: cue card with prompts
            prompts = question_info.get("prompts", [])
            addressed = 0
            for prompt in prompts:
                keywords = re.findall(r'\b\w+\b', prompt.lower())
                keywords = [k for k in keywords if len(k) > 3]
                for k in keywords[:4]:
                    if k in text.lower():
                        addressed += 1
                        break
            
            prompt_count = len(prompts)
            coverage = addressed / max(prompt_count, 1)
            
            if coverage >= 0.75 and word_count >= 100:
                score = 7
                details.append(f"Addressed {addressed}/{prompt_count} prompts, good length ({word_count} words)")
            elif coverage >= 0.5 and word_count >= 60:
                score = 6
                details.append(f"Addressed {addressed}/{prompt_count} prompts, adequate length")
            else:
                score = 5
                details.append(f"Addressed only {addressed}/{prompt_count} prompts, short response")
            
            if word_count >= 150:
                details.append("Exceeds 2-min target length")
        
        return {
            "score": score,
            "word_count": word_count,
            "details": "; ".join(details)
        }
    
    def calculate_overall_band(self, scores, weights=None):
        """Calculate overall IELTS band score."""
        if weights is None:
            weights = {
                "fluency": 0.25,
                "vocabulary": 0.20,
                "grammar": 0.20,
                "pronunciation": 0.15,
                "task_achievement": 0.20
            }
        
        weighted_sum = sum(
            scores.get(k, 0) * weights.get(k, 0)
            for k in weights
        )
        
        # IELTS bands are in 0.5 increments
        band = round(weighted_sum * 2) / 2
        band = max(1, min(9, band))
        
        return band
    
    def evaluate_full_response(self, text, question_info, part=1):
        """Complete evaluation of a speaking response."""
        
        fluency = self.analyze_fluency(text)
        vocab = self.analyze_vocabulary(text)
        grammar = self.analyze_grammar(text)
        pronunciation = self.analyze_pronunciation(text)
        task = self.analyze_task_achievement(text, question_info)
        
        scores = {
            "fluency": fluency["score"],
            "vocabulary": vocab["score"],
            "grammar": grammar["score"],
            "pronunciation": pronunciation["score"],
            "task_achievement": task["score"]
        }
        
        overall = self.calculate_overall_band(scores)
        
        # Duration check
        wpm = 140
        estimated_duration = self.estimate_speaking_duration(text, wpm)
        meets_duration = (part == 1 and estimated_duration >= 25) or \
                        (part == 2 and estimated_duration >= 60) or \
                        (part == 3 and estimated_duration >= 30)
        
        passed = overall >= 7.0 and meets_duration
        
        # Safety: ensure minimum score of 3 for any criterion
        for k in scores:
            scores[k] = max(3.0, scores[k])
        return {
            "overall_band": overall,
            "scores": scores,
            "details": {
                "fluency": fluency["details"],
                "vocabulary": vocab["details"],
                "grammar": grammar["details"],
                "pronunciation": pronunciation["details"],
                "task_achievement": task["details"]
            },
            "estimated_duration_seconds": round(estimated_duration),
            "meets_duration_requirement": meets_duration,
            "word_count": fluency["word_count"],
            "passed": passed
        }
    
    def generate_feedback(self, evaluation):
        """Generate human-readable feedback from evaluation results."""
        feedback_parts = []
        overall = evaluation["overall_band"]
        scores = evaluation["scores"]
        details = evaluation["details"]
        
        if evaluation["passed"]:
            feedback_parts.append(f"✅ OVERALL: Band {overall} - PASSED! Great work!")
        else:
            if overall < 7.0:
                feedback_parts.append(f"❌ OVERALL: Band {overall} - Below 7.0 target")
                feedback_parts.append(f"   You need to improve.")
            else:
                feedback_parts.append(f"⚠️  OVERALL: Band {overall} - Good score but duration issue")
        
        # Criteria breakdown
        feedback_parts.append(f"\n📊 Detailed Scores (Target: Band 7):")
        criteria_names = {
            "fluency": "Fluency & Coherence",
            "vocabulary": "Lexical Resource",
            "grammar": "Grammatical Range",
            "pronunciation": "Pronunciation",
            "task_achievement": "Task Achievement"
        }
        
        for key, name in criteria_names.items():
            score = scores.get(key, 0)
            detail = details.get(key, "")
            icon = "✅" if score >= 7 else ("⚠️" if score == 6 else "❌")
            feedback_parts.append(f"  {icon} {name}: {score}/9 - {detail[:100]}")
        
        if evaluation["meets_duration_requirement"]:
            feedback_parts.append(f"✅ Duration: {evaluation['estimated_duration_seconds']}s (meets target)")
        else:
            target = "25s" if evaluation["estimated_duration_seconds"] < 25 else "60s (Part2)/30s (Part1/3)"
            feedback_parts.append(f"❌ Duration: {evaluation['estimated_duration_seconds']}s (below target)")
        
        return "\n".join(feedback_parts)
