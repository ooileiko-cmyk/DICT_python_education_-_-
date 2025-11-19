print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.\n")
camel = r"""
г  ___.-''''-.
г /___  @    |
г ',,,,.     |         _.'''''''._
г     '     |        /           \
г     |     \    _.-'             \
г     |      '.-'                  '-.
г     |                               ',
г     |                                '',
г      ',,-,                           ':;
г           ',,| ;,,                 ,' ;;
г              ! ; !'',,,',',,,,'!  ;   ;:
г             : ;  ! !       ! ! ;  ;   :;
г             ; ;   ! !      ! !  ; ;   ;,
г            ; ;    ! !     ! !   ; ;
г            ; ;    ! !    ! !     ; ;
г           ;,,      !,!   !,!     ;,;
г           /_I      L_I   L_I     /_I
"""
lion = r"""
г   ,w.
г ,YWMMw  ,M  ,
г  M      mm
г'  YMMMM.   MM
г     YMMMb  MM
г      MMMMM MM
г      MMMMMM'
г       'MMMM'
г         MM
г         MM
"""

deer = r"""
г   /|       |\
г__\\       //__'
г   ||      ||
г \__\     |'__/
г   `_\\   //_'
г   _.,:---;,._
г   \_:     :_/
"""

goose = r"""
г
г
г
"""

bat = r"""
г
г
г
"""

rabbit = r"""
г
г
г
"""
animals = [camel, lion, deer, goose, bat, rabbit]
while True:
    num = input("Please enter the number of the habitat you would like to view (or 'exit' to quit): ")
    if num == "exit":
        print("You've reached the end of the program.")
        break
    if num.isdigit():
        num = int(num)
        if 0 <= num < len(animals):
            print(animals[num])
        else:
            print("Invalid number. Try again.")
    else:
        print("Invalid input. Enter a number or 'exit'.")