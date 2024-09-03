# Lesson 20. Abstracts and polymorphism

from abc import ABC, abstractmethod


class Industry(ABC):
    def __init__(self, sphere, business_scope):
        self.sphere = sphere
        self.business_scope = business_scope

    @abstractmethod
    def company_main_business(self):
        pass

    @abstractmethod
    def annual_income(self):
        pass


class BlueberryIndustry(Industry):
    def __init__(self, sphere, business_scope, additional_sphere, main_product, production_volume, product_price,
                 new_product, processed_production_volume, processed_product_price):
        super().__init__(sphere, business_scope)
        self.additional_sphere = additional_sphere
        self.main_product = main_product
        self.product_volume = production_volume                      # volume in ton
        self.product_price = product_price                           # AMD per KG
        self.new_product = new_product
        self.processed_product_volume = processed_production_volume  # volume in box:standard 300ml 20jars within
        self.processed_product_price = processed_product_price       # AMD per jar

    def company_main_business(self):
        return (f"Doing business mainly {self.business_scope} in {self.sphere} since 1996 \nthe Company has expanded "
                f"its scope from {self.main_product} production and sales to \n"
                f"{self.new_product} production in {self.additional_sphere}.")

    def annual_income(self):
        agriculture_income = self.product_price * self.product_volume * 1000
        factory_income = self.processed_product_price * self.processed_product_volume * 20
        return f"The annual income of the Company counts: {agriculture_income + factory_income: 6.2f} AMD."


class Tourism(Industry):
    def __init__(self, sphere, business_scope, main_product, standard_pack_quantity,
                 std_subscribed_discount_quantity, std_corporate_discount_quantity, standard_pack_price,
                 business_pack_quantity, business_sub_discount_quantity,
                 business_corp_discount_quantity, business_pack_price, subscription_discount=8, corporate_discount=16):
        super().__init__(sphere, business_scope)
        self.main_product = main_product
        self.standard_package_quantity = standard_pack_quantity                 # annual quantity without discount
        self.standard_sub_discount_quantity = std_subscribed_discount_quantity  # annual quantity with sub_discount
        self.standard_corp_discount_quantity = std_corporate_discount_quantity  # annual quantity with corp_discount
        self.standard_package_price = standard_pack_price                       # AMD per person (package = ticket)
        self.business_class_package_quantity = business_pack_quantity           # annual quantity without discount
        self.business_sub_discount_quantity = business_sub_discount_quantity    # annual quantity with sub_discount
        self.business_corp_discount_quantity = business_corp_discount_quantity  # annual quantity with corp_discount
        self.business_class_package_price = business_pack_price                 # AMD per person (package = ticket)
        self.subscription_discount = subscription_discount                      # annual subscription discount in %
        self.corporate_discount = corporate_discount                            # corporate discount in %

    def company_main_business(self):
        return (f"The Company specialized in {self.sphere} is well-known {self.business_scope} "
                f"providing {self.main_product}.")

    def annual_income(self):
        standard_package_income = (self.standard_package_quantity * self.standard_package_price +
                                   (self.standard_sub_discount_quantity * self.standard_package_price *
                                    (1 - self.subscription_discount / 100)) +
                                   (self.standard_corp_discount_quantity * self.standard_package_price *
                                    (1 - self.corporate_discount / 100)))
        business_package_income = (self.business_class_package_quantity * self.business_class_package_price +
                                   (self.business_sub_discount_quantity * self.business_class_package_price *
                                    (1 - self.subscription_discount / 100)) +
                                   (self.business_corp_discount_quantity * self.business_class_package_price *
                                    (1 - self.corporate_discount / 100)))
        return (f"The annual total income from Standard Package sales for the year 2023 was "
                f"{standard_package_income} AMD,"
                f"from Business Class Package sales it amounted {business_package_income} AMD. \n"
                f"The Company had in total"
                f"{standard_package_income + business_package_income: 4.2f} AMD income in 2023.")


blueberry_magic = BlueberryIndustry("Agriculture", "Nationwide",
                                    "Food Processing Industry", "Blueberry", 4,
                                    10000, "BlueberryJam", 100,
                                    6500)
nature_tourism_agency = Tourism("Tourism", "Nationwide",
                                "Tourism and travel-related services", 2700,
                                1400, 2500, 15000,
                                1900, 2000, 4500,
                                20000)

print(blueberry_magic.company_main_business())
print(blueberry_magic.annual_income())

print(nature_tourism_agency.company_main_business())
print(nature_tourism_agency.annual_income())
