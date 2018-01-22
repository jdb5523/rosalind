s = open("data.txt").read()
reverse = s[::-1]
complement = str.maketrans("ATCG", "TAGC")
print(reverse.translate(complement))