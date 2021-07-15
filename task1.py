# დაწერეთ ფუნქცია, რომელსაც გადაეცემა string-ი და აბრუნებს True-ს თუ
# გადაცემული string-ი პალინდრომია, წინააღმდეგ შემთხვევაში False-ს. პალინდრომი
# არის ტექსტი რომელიც ერთნაირად იკითხება ორივე მხრიდან, მაგ: radar, level,
# rotor, abcdcba.

# დავუშვებ რომ შემოსული srting იქნება ერთი სიტყვა, whitespace-ის გარეშე.
def is_palindrome(string: str) -> bool:
    i, j = 0, len(string) - 1
    while(i < j):
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

testcases = [
        "radar", "level", "rotor", "abcdcba", "abba", "a", "ab", "hello", "lee"
        ]

for testcase in testcases:
    print(testcase, is_palindrome(testcase))
