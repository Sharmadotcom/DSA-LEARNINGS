class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Calculates the minimum number of people to teach so that all friends can communicate.
        """
        
        # Convert each user's language list to a set for fast lookups.
        lang_sets = [set()] + [set(lang) for lang in languages]
        
        # Find all users who are in a friendship where they can't communicate.
        target_users = set()
        for u, v in friendships:
            if not lang_sets[u].intersection(lang_sets[v]):
                target_users.add(u)
                target_users.add(v)

        if not target_users:
            return 0
            
        # For each language, count how many people in our target group would need to learn it.
        min_teach_count = float('inf')
        
        for lang_id in range(1, n + 1):
            current_teach_count = 0
            for user_id in target_users:
                if lang_id not in lang_sets[user_id]:
                    current_teach_count += 1
            
            min_teach_count = min(min_teach_count, current_teach_count)
            
        return min_teach_count