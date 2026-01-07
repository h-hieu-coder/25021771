class ShoppingCart:
    def __init__(self):
        self.products = []

    def add(self):
        name = input("Tên sản phẩm: ")
        price = float(input("Đơn giá: "))
        self.products.append({"name": name, "price": price})

    def delete(self):
        name = input("Nhập tên sản phẩm cần xóa: ")
        for sp in self.products:
            if sp["name"] == name:
                self.products.remove(sp)
                print("Đã xóa sản phẩm")
                return
        print("Không tìm thấy sản phẩm")

    def check(self):
        if len(self.products) == 0:
            print("Giỏ hàng rỗng")
        else:
            print("Giỏ hàng có", len(self.products), "sản phẩm")

    def tong_tien(self):
        total = sum(sp["price"] for sp in self.products)
        print("Tổng tiền:", total)

    def hien_thi(self):
        if not self.products:
            print("Giỏ hàng rỗng")
            return
        print("Tên".center(15), "Giá".center(10))
        for sp in self.products:
            print(sp["name"].center(15), str(sp["price"]).center(10))

    def clear(self):
        self.products.clear()
        print("Đã xóa toàn bộ giỏ hàng")
cart = ShoppingCart()

while True:
    print("""
    2. Thêm sản phẩm
    3. Xóa sản phẩm
    4. Kiểm tra giỏ hàng
    5. Tính tổng tiền
    6. Hiển thị sản phẩm
    7. Xóa toàn bộ giỏ hàng
    """)

    choice = int(input("Lựa chọn: "))

    if choice == 2:
        cart.add()
    elif choice == 3:
        cart.delete()
    elif choice == 4:
        cart.check()
    elif choice == 5:
        cart.tong_tien()
    elif choice == 6:
        cart.hien_thi()
    elif choice == 7:
        cart.clear()

    x = input("Có muốn thoát khỏi chương trình không? ")
    if x.lower() == "yes":
        break
