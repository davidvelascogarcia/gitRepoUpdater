'''
  * ***************************************************************
  *      Program: Git Repo Updater
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import datetime
import os
import platform
import sys
import time

print("")
print("")
print("**************************************************************************")
print("**************************************************************************")
print("                       Program: Git Repo Updater                          ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading gitRepoUpdater engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")
systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

# Get initial time
initialTime = datetime.datetime.now()

print("")
print("**************************************************************************")
print("Update Local Repositories")
print("**************************************************************************")
print("")
print("[INFO] Searching local repositories ...")
print("")

# Go to root path
try:
    os.chdir("./../../")

except:
    print("")
    print("[ERROR] Error moving to root path.")
    print("")

# Variable to count repo updated
repoUpdatedCount = 1

# Update all local repositories in root path
for repositorie in os.listdir("."):

    print("")
    print("[INFO] Local repositorie founded: " + str(repositorie))
    print("")

    print("")
    print("**************************************************************************")
    print("Updating repositorie " + str(repositorie))
    print("**************************************************************************")
    print("")
    print("[INFO] Updating repositorie " + str(repositorie) + ", " + str(repoUpdatedCount) + "/" + str(len(os.listdir("."))) + " ...")
    print("")

    # Move to local path
    try:
        os.chdir(str(repositorie))

    except:
        print("")
        print("[ERROR] Error moving to " + str(repositorie) + " repositorie.")
        print("")

    # Execute update repositorie
    try:
        os.system("git pull")

        print("")
        print("[INFO] " + str(repositorie) + " repositorie updated correctly.")
        print("")

    except:
        print("")
        print("[ERROR] Error updating " + str(repositorie) + " repositorie.")
        print("")

    # Return to root path
    try:
        os.chdir("./../")

    except:
        print("")
        print("[ERROR] Error moving to root path.")
        print("")

    # Count repoUpdatedCount + 1
    repoUpdatedCount = repoUpdatedCount + 1

print("")
print("**************************************************************************")
print("Local Repositories Updated")
print("**************************************************************************")
print("")
print("[INFO] Local repositories updated correctly.")
print("")

# Get end time
endTime = datetime.datetime.now()

# Get elapsedTime
elapsedTime = endTime - initialTime

print("")
print("[INFO] Elapsed time: " + str(elapsedTime))
print("")

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("gitRepoUpdater program finished correctly. ")
print("")
endProgram = input()
