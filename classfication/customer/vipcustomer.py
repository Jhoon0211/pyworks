# VIPCustomer 클래스 - Customer
from classfication.customer.customer import Customer


class VIPCustomer(Customer):
    def __init__(self, cid, cname, agent):
        super().__init__(cid, cname)
        self.agent = agent
        self.cgrade = "VIP"
        self.sale_ratio = 0.1    # 10%
        self.bonus_ratio = 0.05  # 5%

    def calc_price(self, price):
        # 구매 할인율 (price = price * sale_ratio) (가격 = 가격 * 구매 할인율)
        # 할인된 가격 = 원래 가격 - (원래 가격 * 구매 할인율)
        price -= int(price * self.sale_ratio)
        # 보너스 포인트
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):
        return f'{super().__str__()}\n 전문 상담원 ID는 {self.agent}입니다.'

if __name__=="__main__":
    vip = VIPCustomer(1004, '진', 777)
    price = 10000
    cost = vip.calc_price(price)

    print(f'{vip.cname}님의 구매 비용은 {cost}원 입니다.')
    print(vip)