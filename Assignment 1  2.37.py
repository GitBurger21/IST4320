#Anthony Burger 007196196
#Movie Discount Program 

#Get user input
mov_rent_num = input('Enter the number of Movie Rentals: ')
mem_ref_num = input('Enter the number of members reffered to the video club: ')

#change to float
mov_rent_num = float(mov_rent_num)
mem_ref_num = float(mem_ref_num)                 

discount = mov_rent_num + mem_ref_num

#Make Sure Discount does not exceed 75%
if discount > 75:
    discount = 75
    
print('The discount is equal to:',('%10.2f' %discount),' percent.')
