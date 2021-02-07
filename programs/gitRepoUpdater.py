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
from halo import Halo
import platform


class GitRepoUpdater:

    # Function: Constructor
    def __init__(self):
        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

    # Function: getSystemPlatform
    def getSystemPlatform(self):
        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: repoUpdater
    def repoUpdater(self):

        # Get initial time
        initialTime = datetime.datetime.now()

        print("**************************************************************************")
        print("Update Local Repositories")
        print("**************************************************************************")

        systemResponseMessage = "\n[INFO] Searching local repositories ...\n"
        self.systemResponse.text_color = "blue"
        self.systemResponse.info(systemResponseMessage)

        # Go to root path
        try:
            os.chdir("./../../")

        except:
            systemResponseMessage = "\n[[ERROR] Error moving to root path.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)

        # Variable to count repo updated
        repoUpdatedCount = 1

        # Update all local repositories in root path
        for repo in os.listdir("."):

            systemResponseMessage = "\n[INFO] Local repo founded: " + str(repo) + "\n"
            self.systemResponse.text_color = "blue"
            self.systemResponse.info(systemResponseMessage)

            print("**************************************************************************")
            print("Updating repo " + str(repo))
            print("**************************************************************************")

            systemResponseMessage = "\n[INFO] Updating repo " + str(repo) + ", " + str(repoUpdatedCount) + "/" + str(len(os.listdir("."))) + " ...\n"
            self.systemResponse.text_color = "yellow"
            self.systemResponse.warn(systemResponseMessage)

            # Move to local path
            try:
                os.chdir(str(repo))

            except:
                systemResponseMessage = "\n[ERROR] Error moving to " + str(repo) + " repo.\n"
                self.systemResponse.text_color = "red"
                self.systemResponse.fail(systemResponseMessage)

            # Execute update repo
            try:
                os.system("git pull")

                systemResponseMessage = "\n[INFO] " + str(repo) + " repo updated correctly.\n"
                self.systemResponse.text_color = "green"
                self.systemResponse.succeed(systemResponseMessage)

            except:

                systemResponseMessage = "\n[ERROR] Error updating " + str(repo) + " repo.\n"
                self.systemResponse.text_color = "red"
                self.systemResponse.fail(systemResponseMessage)

            # Return to root path
            try:
                os.chdir("./../")

            except:
                systemResponseMessage = "\n[ERROR] Error moving to root path.\n"
                self.systemResponse.text_color = "red"
                self.systemResponse.fail(systemResponseMessage)

            # Count repoUpdatedCount + 1
            repoUpdatedCount = repoUpdatedCount + 1

        print("**************************************************************************")
        print("Local Repositories Updated")
        print("**************************************************************************")

        systemResponseMessage = "\n[INFO] Local repositories updated correctly.\n"
        self.systemResponse.text_color = "green"
        self.systemResponse.succeed(systemResponseMessage)

        # Get end time and elapsedTime
        endTime = datetime.datetime.now()
        elapsedTime = endTime - initialTime

        systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime) + "\n"
        self.systemResponse.text_color = "blue"
        self.systemResponse.info(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                       Program: Git Repo Updater                          ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading Git Repo Updater engine ...\n")

    # Build cryptoFileSecurityEncoder object
    gitRepoUpdater = GitRepoUpdater()

    # Get system platform
    systemPlatform, systemRelease = gitRepoUpdater.getSystemPlatform()

    # Update repos
    gitRepoUpdater.repoUpdater()

    print("\n**************************************************************************")
    print("Program finished")
    print("**************************************************************************")
    print("\ngitRepoUpdater program finished correctly.\n")

    userExit = input()

if __name__ == "__main__":

    # Call main function
    main()

