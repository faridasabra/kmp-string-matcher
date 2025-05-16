def compute_lps_array(pattern):
    pattern_length = len(pattern)
    lps = [0] * pattern_length
    length = 0
    i = 1

    while i < pattern_length:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    if not pattern or not text:
        return ["Pattern or text is empty"]

    if len(pattern) > len(text):
        return ["Pattern is longer than text"]

    Text_length = len(text)
    pattern_length = len(pattern)

    if pattern_length == 1:
        return [i for i in range(Text_length) if text[i] == pattern[0]]

    lps = compute_lps_array(pattern)
    result = []
    i = 0
    j = 0

    while i < Text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_length:
            result.append(i - j)
            j = lps[j - 1]
        elif i < Text_length and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

if __name__ == "__main__":
    print("-" * 60)
    print("KMP String Matching Algorithm Test")
    print("-" * 60)

    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(f"Text string  : {text}")
    print(f"Pattern      : {pattern}")
    print("-" * 60)
    print("Time Complexity: O(Text_length+m) where Text_length is text length and m is pattern length")
    print("-" * 60)

    positions = kmp_search(text, pattern)

    if positions:
        print(f"Pattern found at positions: {positions}")
        for pos in positions:
            print(f"Text  : {text}")
            print(f"Match : {' ' * pos}{pattern}")
    else:
        print("Pattern not found in the text")

    print("-" * 60)