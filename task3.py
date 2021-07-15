# მოცემულია string-ი რომელიც შედგება “(“ და “)“ ელემენტებისგან. დაწერეთ
# ფუნქცია რომელიც აბრუნებს ფრჩხილები არის თუ არა მათემატიკურად სწორად
# დასმული.
#         მაგ: “(()())” სწორი მიმდევრობაა,  “())()” არასწორია

def are_parentheses_correct(string: str) -> bool:
    parentheses_count = 0
    for char in string:
        if char == ')': parentheses_count -= 1
        elif char == '(': parentheses_count += 1

        # თუ parentheses_count უარყოფითია, იმას ნიშნავს რომ string-ში არსებობს
        # ერთი მაინც ')' რომელსაც არ გააჩნია შესაბამის '(' მარცხნიდან
        if parentheses_count < 0:
            return False

    return parentheses_count == 0

testcases = ["()", "((()))", ")()(", "())()", "((((())))"]
for testcase in testcases:
    print(testcase, are_parentheses_correct(testcase))
