from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faqs import faqs
from preprocess import preprocess

class FAQChatbot:
    def __init__(self):
        self.questions = list(faqs.keys())
        self.answers = list(faqs.values())
        self.vectorizer = TfidfVectorizer()
        
        # Preprocess and vectorize FAQs
        self.processed_questions = [preprocess(q) for q in self.questions]
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)
    
    def get_answer(self, user_query):
        processed_query = preprocess(user_query)
        query_vector = self.vectorizer.transform([processed_query])
        
        # Find most similar FAQ
        similarities = cosine_similarity(query_vector, self.question_vectors)
        best_match_idx = similarities.argmax()
        best_score = similarities.max()
        
        if best_score < 0.3:  # Low confidence threshold
            return "Sorry, I don't understand. Can you rephrase?"
        
        return self.answers[best_match_idx]
def run_cli_chatbot():
    bot = FAQChatbot()
    print("🤖 FAQ Chatbot: Ask me anything! (Type 'quit' to exit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("🤖 Goodbye!")
            break
        
        response = bot.get_answer(user_input)
        print(f"🤖 {response}")

if __name__ == "__main__":
    run_cli_chatbot()