class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)

        words = re.findall(r'\w+', paragraph.lower())

        filtered_words = [word for word in words if word not in banned_set]

        word_counts = Counter(filtered_words)


        return word_counts.most_common(1)[0][0]
