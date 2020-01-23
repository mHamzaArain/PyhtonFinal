def abs_path_finder(exact_file):
        '''To find exact image of alien.'''
        # os.walk -> deeply browse each path, file & folder
        # os.getcd -> current working diecttory
        import os
        finalPath = ''
        for path, folder, file in os.walk(os.getcwd()):
            # Considering each path whose ends with img(i.e; img folder)
            folder = file = None
            if path.endswith('icons'):
                # join path e.g;  "C:\Users\Hamza Arain\Desktop\Alien Project v1.3\Ch12_Firing_fromShip\img" + "/"  + "ship.bmp"  
                finalPath = os.path.join(path, exact_file)
                break
        return finalPath