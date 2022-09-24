title="the invincible"
print(title)

title="captain america - the first avenger"
print(title)


#this capitalizes names
actor="chris evans"
actor="chris pratt"
print(actor.title())
print(actor.upper())
print(actor.lower())

firstname="star"
lastname="lord"
fullname=f"{firstname} {lastname}"
name = f"Hello, {fullname.title()}!"
print(name)


prifirstname="star"
lastname="lord"
fullname=f"{firstname} {lastname}"
name = f"Hello, {fullname.title()}!"
print ("\tStar Lord")


name="guardians of the galaxy - volume I "
print(name.title().rstrip())

name="guardians of the galaxy - volume I "
print(name.title())


quote="The Cap said, ''I can do this all day.''"
print(quote)



quote="The Cap said, ''I can do this all day.''"
famous_person=quote
print(famous_person)


print("\tThe Avengers")
print("\nCaptain America \nIron Man \nThor Odinson \nHawkeye \nBlack Widow \nHulk")



number=45_514_454_545
print(number)

cap, ironman, thor = 4, 7, 1
print(6+2, 9-1, 2*4, 64/8)


avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
print(avengers)

avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
print(avengers[0])

avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
print(avengers[3].title())



avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
print(avengers[-2])


avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
message=f" The first avenger was {avengers[0].title()}."
print(message)


avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
avengers[3]='Hawkeye'
print(avengers)


avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
avengers.append('hawkeye')
print(avengers)


avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
avengers.insert(0, 'hawkeye')
print(avengers)


avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
del avengers[3]
print(avengers)



avengers= ['cap' , 'ironman' , 'thor' , 'hulk']
popped_avengers= avengers.pop()
print(avengers)
print(popped_avengers)


avengers= ['captain america' , 'ironman' , 'thor' , 'hulk']
avengers[3]='spiderman'
popped_avengers= avengers.pop()
firstavenger= avengers.pop(0)
deceased_avengers= 'ironman'
avengers.remove(deceased_avengers)
print(avengers)
print(popped_avengers)
print(f"The newest Avenger is {popped_avengers.title()}.")
print(f"The First Avenger was {firstavenger.title()}.")
print(f"\n {deceased_avengers.title()} is deceased.")



justice_league=['batman' , 'superman' , 'wonderwoman' , 'the flash' , 'martian manhunter' , 'green lantern' , 'green arrow' , 'cyborg' , 'aquaman' , 'steel']
league_members=(justice_league.pop(9))

print(justice_league)



justice_league=['batman' , 'superman' , 'wonderwoman' , 'the flash' , 'martian manhunter' , 'green lantern' , 'green arrow' , 'cyborg' , 'aquaman' , 'steel']
justice_league[9]='robin'
non_members='robin'
justice_league.remove(non_members)
print(justice_league)




print("There's room for more superheroes")

justice_league=['batman' , 'superman' , 'wonderwoman' , 'the flash' , 'martian manhunter' , 'green lantern' , 'green arrow' , 'cyborg' , 'aquaman' , 'steel']
justice_league.insert(0, 'shazam')
justice_league.insert(3, 'someguy')
justice_league.append('somegal')
print(justice_league)
print(sorted(justice_league))
print("\nOops! Spoke too soon. There isn't any more room left.")
justice_league.remove('shazam')
justice_league.remove('someguy')
justice_league.pop()
justice_league.sort()
print(justice_league)
justice_league.reverse()
print(justice_league)
print(justice_league[-5])




vampires = ['\n\n\n\n\n\n' , 'Stefan Salvatore' , 'Damon Salvatore' , 'Niklaus Michealson' , 'Elijah Michealson' , 'Rebekah Michealson' , 'Catherine Pierce' , 'Elena Gilbert' , 'Caroline Forbes' , 'Finn Michealson' , 'Marcel Gerard' , 'Vicki Donovan']
for vampire in vampires:
    print(vampire)
    print(f"{vampire.title()}, is a vampire!")
    print(f"Nice to meet you!, {vampire.title()}.\n")
    
print("They're from The Vampire Diaries")
    
    
    

vampires = ['Stefan Salvatore' , 'Damon Salvatore' , 'Niklaus Michealson' , 'Elijah Michealson' , 'Rebekah Michealson' , 'Catherine Pierce' , 'Elena Gilbert' , 'Caroline Forbes' , 'Finn Michealson' , 'Marcel Gerard' , 'Vicki Donovan']
print(vampires[5:8])
print(vampires[:5])
print(vampires[5:])







