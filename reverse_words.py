def reverse_words(s):
    split_li = s.split(".")
    # print(f"The split list {split_li}")
    cleaned_li = [ele for ele in split_li if len(ele)>0]
    rev_li = cleaned_li[::-1]
    rev_str = ".".join(rev_li)
    return rev_str

s1 = "i.like.this.program.very.much"
res1 = reverse_words(s=s1)
print(f"Input:{s1}\n result :{res1}")

s2 = "..geeks..for.geeks."
res2 = reverse_words(s=s2)
print(f"Input:{s2}\n result :{res2}")

s3 = "..home....."
res3 = reverse_words(s=s3)
print(f"Input:{s3}\n result :{res3}")