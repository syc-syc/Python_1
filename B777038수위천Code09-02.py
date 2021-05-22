coffee=0

def coffee_machine(button):
    print()
    print("#1.(자동으로)뜨거운 물을 준비한다.");
    print("#2.(자동으로)종이컵을 준비한다.");

    if button ==1:
        print("#3.(자동으로)보통커피를 탄다.")
    elif button ==2:
        print("#3.(자동으로)설탕커피를 탄다.")
    elif button ==3:
        print("#3.(자동으로)블랙커피를 탄다.")
    else:
        print("#3.(자동으로)아부거나 탄다./n")

    print()
