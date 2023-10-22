from database import * 

def test_list_all_cards():
    print("Testing list_all_cards...")
    cards = list_all_cards()
    print(cards)

def test_add_new_card():
    print("Testing add_new_card...")
    cardtypeid = 1
    userid = 1
    expiry = '2024-09-22'
    balance = 50
    add_new_card(cardtypeid, userid, expiry, balance)
    print("Card added.")

def test_update_card():
    print("Testing update_card...")
    cardid = 1 
    userid = 1
    cardtypeid = 1
    update_card(cardid, userid, cardtypeid)
    print("Card updated.")

def test_delete_card():
    print("Testing delete_card...")
    cardid = 1 
    delete_card(cardid)
    print("Card deleted.")

def test_cards_expiry_report():
    print("Testing cards_expiry_report...")
    report = cards_expiry_report()
    print(report)

def main():
    test_list_all_cards()
    test_add_new_card()
    test_update_card()
    test_delete_card()
    test_cards_expiry_report()

if __name__ == "__main__":
    main()
