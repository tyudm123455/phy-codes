def velocity (  ) :
    distance = float ( input ( "Enter the distance (in meters ) : " ) )
    time = float ( input ( "Enter the time (in seconds ) : " ) )
    velocity = distance / time
    print (f"The velocity is {velocity} m/s")
def pressure (  ) :
    area = float ( input ( "Enter the area (in m^2 ) : " ) )
    force = float ( input ( "Enter the force (in N ) : " ) )
    pressure = force / area
    print (f"The pressure is {pressure}N/M^2")

def density (  ) :
    mass = float ( input ( "Enter the mass (in kg ) : " ) )
    volume = float ( input ( "Enter the volume (in cm^3 ) : " ) )
    density=mass/volume
    print ( density)
    print ( f"The density is {density}kg/cm^3")

def power (  ) :
    work = float ( input ( "Enter the work (in j ) : " ) )
    time = float ( input ( "Enter the time (in s ) : " ) )  
    power=work/time
    print ( power)
    print ( f"The power is {power} j/s")

def work (  ) :
    force = float ( input ( "Enter the force (in N ) : " ) )
    distance = float ( input
    ("Enter the distance (in M ) : " ) )
    work = force*distance
    print ( work)
    print ( f"The work is {work} NM")

while True:
    print ( "Physics Calculator")

    formulae=["1.Velocity", "2.Pressure","3.Density","4.Power","5.Work"]
    for form in formulae:
        print ( form)
    entry= input ( "Enter a quantity: ")
    if entry=="1":
        velocity ( )
    elif entry=="2":
        pressure ( )
    elif entry=="3":
        density ( )
    elif entry=="4":
        power ( )
    elif entry=="5":
        work ( )        
    else:
        print ( "Input a valid quantity")
    
    again = input ( "Do you want to calculate something else? (yes or no ) : ")
    if again.lower (  ) =="yes":
        continue
    elif again.lower ( ) == "no":
        print ( "Thank you")
        break

    else:
        print ( "Invalid input")
        break