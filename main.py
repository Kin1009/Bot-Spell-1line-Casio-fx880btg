import chars
print("Helo :)) Đây là tool để spell 1 line tiếng việt trên CASIO 880")
input_text = input("Nhập chữ cần spell: ")[:17]
#input_text = "Nguyễn Minh Khôi"
needed_for_center = input("Có căn giữa không? [Y/n]: ").lower()
#needed_for_center = "y" 
need_guide = input("Có cần hướng dẫn không? [Y/n]: ").lower()
#need_guide = "y"
want_inverted = input("Có muốn chữ background đen không? [Y/n]: ").lower()
#want_inverted = "n"
if needed_for_center == "y" or needed_for_center == "":
    needed_for_center = True
else:
    needed_for_center = False
if need_guide == "y" or need_guide == "":
    need_guide = True
else:
    need_guide = False
if want_inverted == "y" or want_inverted == "":
    want_inverted = True
else:
    want_inverted = False
length_of_text = len(input_text)
space_start = 0
space_end = 0
if needed_for_center:
    space_start = (17 - length_of_text) // 2
    space_end = 17 - length_of_text - space_start
else:
    space_end = 17 - length_of_text
input_text = " " * space_start + input_text + " " * space_end
print("Xử lí chuỗi: " + input_text)
hex_string = ""
for char in input_text:
    hex_string += chars.chars_dict.get(char, "00") + " "
print("Hex: " + hex_string.strip())
hex_string = [i for i in hex_string.split(" ") if i]
sect1 = hex_string[:8]
sect2 = hex_string[8:16]
sect3 = hex_string[16:24]
print("20E3: " + " ".join(sect1))
print("28E3: " + " ".join(sect2))
print("30E3: " + " ".join(sect3))
print()
if need_guide:
    print(
"""0. Chuẩn bị kiến thức
[vv]: Danh mục xuống (nút có 2 mũi tên xuống)
[^^]: Danh mục lên (nút có 2 mũi tên lên)

Lấy hex:
- Đưa con trỏ vào đằng sau dấu phân số bị lỗi (basic overflow)
Công thức chung của các hằng số hex:
    [CATALOG] [vv] [vv] [OK] [v] [v] [OK] [vv]
Khi lấy hex nhập công thức chung trc
- A: [^] [OK]
- B: [^] [>] [OK]
- C: [OK]
- D: [>] [OK]
- E: [v] [OK]
- F: [v] [>] [OK]
Lấy hằng số xong thì [<] [<] [>] [9] [DEL]
LẤY 1 HEX 1 LẦN
Nhớ: Lấy hex từ phải sang trái, hoặc theo chỉ dẫn
Lấy ABCDBC -> Lấy CBDCBA (trái -> phải)
Ví dụ: Lấy ECEF (Lấy FECE trái -> phải)
[CATALOG] [vv] [vv] [OK] [v] [v] [OK] [vv]
[v] [OK]
[<] [<] [>] [9] [DEL]
[CATALOG] [vv] [vv] [OK] [v] [v] [OK] [vv]
[OK]
[<] [<] [>] [9] [DEL]
[CATALOG] [vv] [vv] [OK] [v] [v] [OK] [vv]
[v] [OK]
[<] [<] [>] [9] [DEL]
[CATALOG] [vv] [vv] [OK] [v] [v] [OK] [vv]
[v] [>] [OK]
[<] [<] [>] [9] [DEL]
Lấy hết hex thì [DEL] [DEL] để xoá overflow
và nhập giá trị

Lưu biến:
Bấm [VARIABLE]
Chọn biến muốn lưu
[OK] [OK]
Trong file, các kí tự như ->A hay ->B ... là lưu vào A, B...

Xong r đó :) Làm đi
""")

hex_table = {
    "A": "[^] [OK]",
    "B": "[^] [>] [OK]",
    "C": "[OK]",
    "D": "[>] [OK]",
    "E": "[v] [OK]",
    "F": "[v] [>] [OK]"
}
result = """
Reset máy:
[SETTINGS] [v] [v] [OK] [vv] [OK] [OK] [OK]
"""
mode68 = """Vào mode68
[SETTINGS] [v] [v] [OK] [vv] [OK] {[OK] và [ON] cùng lúc}
Nếu ko thấy biểu tượng căn ở thanh công cụ là đúng, nếu thấy / bị ra màn hình chính thì làm lại
[5] [Phân số] [6] [EXE] [SETTINGS] {[OK] x3} [HOME] [OK] [^]
Basic overflow:
[<] [DEL] [<] [DEL] [Phân số] [>] [<]
"""
def nhaphex(address, data):
    data = "".join(data)
    result = f"""{mode68}Lấy các kí tự sau:
FECE (trái -> phải)
Nhập:
E.00849608001CEF386401
[EXE]
Lưu biến C
[AC] [^] [<]
Xoá hết chừng nào còn 2 chữ E (EE):
([DEL] x7) [<] ([DEL] x13) [>]
Nhập:
E.[14 số 0]{address}
[EXE]
Lưu biến A
[AC] [v] [<]
[DEL] [<] [DEL] [Phân số] [>] [<]
Lấy các kí tự sau:
AAAE (trái -> phải)
Nhập:
E.00A5968A96148A
[EXE]
Lưu biến B
[AC] [v] [<]
[DEL] [<] [DEL] [Phân số] [>] [<]
Lấy kí tự:
C
Nhập:
1.005C3304
[EXE]
Lưu biến D
[AC] """
    hexes = []
    for i in data:
        if i in ["A", "B", "C", "D", "E", "F"]:
            hexes.append(i)
    hexes = "".join(hexes)[::-1]
    if hexes != "":
        result += f""" [v] [<]
[DEL] [<] [DEL] [Phân số] [>] [<]
Lấy các kí tự sau:
{hexes} (trái -> phải)"""
    result += f"""
Nhập:
1.{data}
[EXE]
Lưu biến E
[AC] [v] [<]
[DEL] [<] [DEL] [Phân số] [>] [<]
Lấy an( :
[CATALOG] [vv] [vv] [OK] [OK] [OK] [<] [<] [>] [CATALOG] [vv] [vv] [OK] [OK] [>] [v] [v] [OK]
[^^] [DEL] [DEL] [>] [CATALOG] [vv] [vv] [v] [OK] [vv] [vv] [OK] [>] [v] [v]
[<] [<] [>] [9] [DEL] [<] [>] [9] [DEL] [vv] [DEL]
[^^]
Nhập:
sin(1an1234567890ln(g((3400g(0g(
Lưu ý 1: Ko đc dùng dâu ( trên bàn phím, ( đã cho sẵn rồi
Lưu ý 2: g( là [FUNCTION] [v] [OK]
Lưu ý 3: ln( là [SHIFT] [logab]
[EXE]
Nếu thấy hiện AC Break là thành công
[AC] [ON]
"""
    return result

result += nhaphex("20E3", sect1)
result += nhaphex("28E3", sect2)
result += nhaphex("30E3", sect3)

end = f"""End:
{mode68}
Lấy kí tự:
E
Nhập:
1.305633040020E300900{"3" if want_inverted else "0"}
[EXE]
Lưu biến A
[AC] [v] [<]
[DEL] [<] [DEL] [Phân số] [>] [<]
Lấy các kí tự sau:
CE (trái -> phải)
Nhập:
E0.038640100009000906C08
[EXE]
Không lưu biến
[AC] [v] [<]
[DEL] [<] [DEL] [Phân số] [>] [<]
Lấy an(B :
[CATALOG] [vv] [vv] [OK] [v] [v] [OK] [vv] [^] [>] [OK] [<] [<] [>] [CATALOG] [vv] [vv] [OK] [OK] [>] [v] [v] [OK]
[^^] [DEL] [DEL] [>] [CATALOG] [vv] [vv] [v] [OK] [vv] [vv] [OK] [>] [v] [v]
[<] [<] [>] [9] [DEL] [<] [>] [9] [DEL] [vv] [DEL]
[^^]
Nhập:
sin(1an1234567890(g(ln(B1
[EXE]
Chúc bạn thành công :)
"""
print(result + end)