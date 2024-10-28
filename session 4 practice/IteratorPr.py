list1=  [2,4,6,8,90]

# create a iterator practice_code/session4/IteratorPr.py

iterator  = iter(list1)

while True:
    try:
        print(next(iterator))
    except StopIteration: # when there is end of list StopIteration will occur
        break


# create a custom iterable in python 


class Team:
      def __init__(self):
           self._members=list()
      def add_members(self, member):
           self._members+=member
      def __iter__(self):
        #    print("i am call iter")
           return TeamMember(self)  # here we pass self keyword to another class
      
class TeamMember:
     def __init__(self, team): # for intializing the object class
          self._team= team
          self.index=0 # for loop iterations 
     def __next__(self):
        #   print("i am call next")
          if self.index < len(self._team._members):
                result= self._team._members[self.index]
                self.index+=1
                return result
          raise StopIteration
     def __iter__(self):
          return self

team = Team()
team.add_members(["Dwarkesh", "Gautam","Rakshit"])

for t in team:
     print(t)




# another way to create a iterator in python 
print("---------------------------------")
class TeamMate:
     
     def __init__(self):
          self.team_member=list()
          self.index=0

     def add_members(self, member):
           self.team_member+=member

     def __iter__(self):
          print("I am calling as iter ")
          return self
     
     def __next__(self):
            if self.index < len(self.team_member):
                print("I am calling as next ")
                self.index+=1
                return next(self)
            raise StopIteration
            
     
          

t1= TeamMate()
t1.add_members(["Dwarkesh", "Gautam","Rakshit"])
for member in t1:
     print(member)


    


    


               
            

               
          
         







