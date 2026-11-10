# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         # print("strs", strs)
#         deli = '2w#@$#e#@$#3s#@$#a#@$#y#@$#1:#'
#         enc_str = []
#         for stri in strs:
#             n = len(stri)
#             x=len(str(n))
#             word = f'{x}{n}'
#             for i in stri:
#                 word=word+i+deli
#             enc_str.append(word)
#         # print("enc_str",enc_str)
#         encoded_string = "".join(enc_str)
#         # print("encoded_string",encoded_string)
#         return encoded_string

#     def decode(self, s: str) -> List[str]:
#         # print("s",s)
#         deli = '2w#@$#e#@$#3s#@$#a#@$#y#@$#1:#'
#         s = s.replace(deli,"")
#         # print("s",s)
#         decoded_list = []
#         def string_len(s):
#             # print("in string_len")
#             # print("s",s)
#             k = 2
#             num_index = 1
#             n = 0
#             x=int(s[0])
#             while(1):
#                 if x<1:
#                     break
#                 num=s[1:k]
#                 # print("num",num)
#                 if k>len(s):
#                     break
#                 try:
#                     num=int(num)
#                     # print("num",num)
#                 except ValueError:
#                     break
#                 n = num
#                 # print("n",n)
#                 num_index+=1
#                 # print("num_index",num_index)
#                 k+=1
#                 x-=1
#                 # print("k",k)
#             return n, num_index
#         while (1):
#             if not s:
#                 break
#             n, num_index = string_len(s)
#             # print("n",n)
#             # print("num_index",num_index)
#             # print("s",s)
#             word = s[num_index:n+num_index]
#             # print("word",word)
#             decoded_list.append(word)
#             # print("decoded_list",decoded_list)
#             s = s[n+num_index:]
#             # print("s",s)
#         return decoded_list






class Solution:

    def encode(self, strs: List[str]) -> str:
        # print("strs", strs)

        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # print("s",s)
        decoded_list = []
        i = 0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            decoded_list.append(word)

            i=j+1+length
        return decoded_list
