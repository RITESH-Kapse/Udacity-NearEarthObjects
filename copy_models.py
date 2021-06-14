from helpers import cd_to_datetime, datetime_to_str



class NearEarthObject:

    def __init__(self, neo , designation ,name, diameter = float('nan'),hazardous = False):

        self.neo = neo

        #Since neo has designation attribute ,calling neo.designation instead of self.designation

        self.designation = neo.pdes
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous

        self.approaches = []


    @property
    def fullname(self):

        return f"The full name of this NEO is {self.designation} + {self.name}"

    def __str__(self):
        return f"A NearEarthObject NEO has name as {self.name} and diameter of {self.diameter} km and is/is not hazardous is {self.hazardous}."  

    def __repr__(self):
        
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")      


class CloseApproach:

    def __init__(self, neo , time , distance = float('nan'),velocity = float('nan')):
        self.neo = neo
        self.designation = neo.designation
        self.time = cd_to_datetime(time)
        self.distance = distance
        self.velocity = velocity

    @property
    def time_str(self):
        self.time = datetime_to_str(self.time)
        return f" On {self.time} , {self.name} approaches Earth at a distance of {self.distance} au and a velocity of {self.velocity } km/s."

    def __str__(self):
        return f"A CloseApproach is travelling close to earth with distance of {self.distance} au and velocity of {self.velocity} "

    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")