from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:

    def __init__(self,designation ,name, diameter = float('nan'),hazardous = False):

        if designation == '':
            self.designation = None
        else:
            self.designation = designation

        if name == '':
            self.name =  None
        else:
            self.name = name

        if not diameter :
            self.diameter = float('nan')
        else:
            self.diameter = diameter

        if not hazardous:
            self.hazardous = False
        else:
            if hazardous == 'N':
                self.hazardous = False
            else:
                self.hazardous = True

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
        self.time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.

        if not distance :
            self.distance = float('nan')
        else:
            self.distance = distance

        if not velocity :
            self.velocity = float('nan')
        else:
            self.velocity = velocity

    @property
    def time_str(self):
        return datetime_to_str(self.time)
       
    def __str__(self):
        return f"A CloseApproach is travelling close to earth with distance of {self.distance} au and velocity of {self.velocity} "

    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
