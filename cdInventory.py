#------------------------------------------#
# Title: Assignment 08
# Desc: CD Inventory with Classes and Methods
# Change Log: (Who, When, What)
# J.Kim, 2022-12-03, created file
# J.Kim, 2022-12-04, added docstrings and comments
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'  # data storage file
lstOfCDObjects = []


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    def __init__(self, cdID, title, artist):
        """Initialize a CD object

        Args:
            cdID (_type_): _description_
            title (_type_): _description_
            artist (_type_): _description_
        """        
        self.__cd_id = cdID
        self.__cd_title = title
        self.__cd_artist = artist
        
    @property
    def cd_id(self): # property for ID
        return self.__cd_id
    
    @cd_id.setter #for future updates to IDs rather than deleting the row
    def cd_id(self, new_id):
        self.__cd_id = new_id
        
    @property
    def cd_title(self): # property for cd title
        return self.__cd_title
    
    @cd_title.setter #for future updates to title without deleting a row
    def cd_title(self, new_title):
        self.__cd_title = new_title
        
    @property
    def cd_artist(self): # property for artist
        return self.__cd_artist
    
    @cd_artist.setter #for future updates to artist rather than deleting the row
    def cd_artist(self, new_artist):
        self.__cd_artist = new_artist
        
#    def __del__(self):
#        print('CD ID: ' + str(self.__cd_id) + " deleted")
        

# -- PROCESSING -- #
class DataProcessor:
    """Processing data for inventory"""

    @staticmethod
    def add_CD(self):
        """Function to create a dictionary row from user inputs and append to list
        Args:
            None.
        Returns:
            None.
        """
        intID, album, artist = IO.user_input(IO)
        new_cd = CD(intID, album, artist)
        lstOfCDObjects.append(new_cd)
        
    @staticmethod
    def cd_delete(self, delete_id):
        """Function to search for the CD user wants to delete, if the matching ID for the CD is found, delete row
        Args:
            CD user wants to delete
        Returns:
            None.
        """
        for i in range(len(lstOfCDObjects)): 
            if lstOfCDObjects[i].cd_id == delete_id: 
                del lstOfCDObjects[i]
                break


class FileIO:
    """Processing the data to and from text file
    properties:
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """
    @staticmethod
    def save_inventory(self, file_name, lst_Inventory):
        """Function to save list of dictionaries to file
        Args:
            None.
        Returns:
            None.
        """
        with open(file_name, 'w') as f:
            for cd in lst_Inventory:
                f.write(str(cd.cd_id) + ',' + cd.cd_title + ',' + cd.cd_artist + '\n')
            f.close()

    @staticmethod
    def load_inventory(self, file_name):
        """Function to manage data ingestion from file to a list of CD objects.
        Args:
            file_name: name of file
        Returns:
            None.
        """
        
        try:
            with open(file_name, 'r') as f:
                lstOfCDObjects.clear()
                for line in f.readlines():
                    lines = line[:-1].split(',')
                    lstOfCDObjects.append(CD(int(lines[0]), lines[1], lines[2])) 
        except:
            print('\nNo data in the file. There is nothing to load.')




# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu(self):
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory\n[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice(self):
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('What would you like to do? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def disp_inv(self, table):
        """Displays current inventory table
        Args:
            table: Refers to the table where the data is temporarily stored
        Returns:
            None.
        """
        print('======= Current Inventory: =======')
        print('ID\tAlbum (by: Artist)\n')
        for cd in lstOfCDObjects:
            print(str(cd.cd_id) + '\t' + cd.cd_title + ' (by: ' + cd.cd_artist + ')')
        print('======================================')


    @staticmethod
    def user_input(self):
        """Asks user to input values for ID, Album, and Artist
        Args:
            None
        Returns:
            User inputs for ID, Album, and Artist name
        """

        while True:
            try:
                cd_id = int(input('Enter ID: '))
            except ValueError as e:
                print('\nYou must enter an integer to continue.\n\n\n') # added context
                continue
            album = input('Enter the title of the album: ').lstrip().rstrip()
            artist = input('Enter the name of the artist: ').lstrip().rstrip()
            
            return cd_id, album, artist
          

# -- Main Body of Script -- #    
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(FileIO, strFileName)

# Display menu to user
while True:
    IO.print_menu(IO)
    uChoice = IO.menu_choice(IO)

    if uChoice == 'x':
        break

    if uChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ').lower().strip()
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(FileIO, strFileName)
            IO.disp_inv(IO, lstOfCDObjects)
        else:
            input('canceling...Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.disp_inv(IO, lstOfCDObjects)
        continue  # start loop back at top.

    elif uChoice == 'a':

        DataProcessor.add_CD(DataProcessor)
        IO.disp_inv(IO, lstOfCDObjects)
        continue  # start loop back at top.

    elif uChoice == 'i':
        IO.disp_inv(IO, lstOfCDObjects)
        continue  # start loop back at top.

    elif uChoice == 'd':
        IO.disp_inv(IO, lstOfCDObjects)
        print('\n\n')
        while True:
            try:
                delete_id = int(input('Which ID would you like to delete? ').strip())
                break
            except ValueError as e:
                print('\nYou must enter an integer value for the ID.\n\n\n')
                continue
        DataProcessor.cd_delete(DataProcessor, delete_id)
        IO.disp_inv(IO, lstOfCDObjects)
        continue  # start loop back at top.

    elif uChoice == 's':
        FileIO.save_inventory(FileIO, strFileName, lstOfCDObjects)
        continue  # start loop back at top.
        
    else:
        print('General Error')
