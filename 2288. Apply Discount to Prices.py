class Solution:
    def discountPrices(self, sentence, discount):
        words = sentence.split(" ")
        prices = []
        discount = discount / 100
        for word in words:
            if self.isNumber(word):
                prices.append(word[1:])
        while '' in prices:
            prices.remove('')
        old_prices = prices.copy()
        for price in range(len(prices)):
            prices[price] = float(prices[price])
            prices[price] -= prices[price] * discount
            prices[price]  = "{:.2f}".format(prices[price])
        all_prices = {}
        for index in range(len(prices)):
            all_prices[old_prices[index]] = prices[index]
        for word in range(len(words)):
            if self.isNumber(words[word]):
                if words[word][1:] in all_prices and words[word][0] == "$":
                    words[word] = all_prices.get(words[word][1:])
                    words[word] = "$" + words[word]
        sentence = ""
        for i in words:
            sentence += i
            sentence += " "
        return sentence[0:-1]
    def isNumber(self, number):
        for digit in number[1:]:
            if digit not in "1234567890 ":
                return False
        return True


str = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
discount = 50
Test = Solution()
print(Test.discountPrices(str, discount))