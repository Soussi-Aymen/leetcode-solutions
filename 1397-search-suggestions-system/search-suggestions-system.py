class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        condidates = sorted(products)
        prefix = ""
        result = []

        for char in searchWord:
            prefix += char
            #filter condidates
            condidates = [condidate for condidate in condidates if condidate.startswith(prefix)]
            #take only the first 3
            result.append(condidates[:3]) 
            
        return result