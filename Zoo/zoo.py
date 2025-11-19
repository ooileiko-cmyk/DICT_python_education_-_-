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
г   _\\   //_'
г   _.,:---;,._
г   \_:     :_/
"""

goose = r"""
г
г     _
г  __(.)<
г  \___)
г
"""

bat = r"""
г   /\                 /\
г  / \'._   (\_/)   _.'/ \
г /_.''._'--('.')--'_.''._\
г | \_ / ;=/ " \=; \ _/ |
г  \/ \__|\___/|__/`  \/
г       \(/|\)/  
"""

rabbit = r"""
г (\_/)
г ( •_•)
г / ><\
"""
animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    num = input("Please enter the number of the habitat you would like to view (0-5) or 'exit' to quit: ")
    if num.lower() == "exit":
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
        print("You've reached the end of the program.")