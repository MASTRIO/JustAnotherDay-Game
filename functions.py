###########################################
#                                         #
#       The Function List for JAGAC       #
#                                         #
###########################################

# * Import Stuff
import variables as Jvar
import itemAPI as Jitems
import commandSystem as Jcommands
import debugCommands as Dcommands
import resources as Jres

# * Functions
# Commands
def COMMAND_LIST(command):
    # Normal Commands
    Jcommands.chelp(command)
    Jcommands.cversion(command)
    Jcommands.cbalance(command)
    Jcommands.cinventory(command)
    Jcommands.cshop(command)
    Jcommands.csettings(command)
    # Debug Commands
    Dcommands.cdebug(command)
    Dcommands.caddResources(command)
    return

# Items
def ITEM_LIST(access):
    Jvar.LOADED_RESOURCE_AMOUNT = Jres.shiny_gems
    Jitems.newItem(access,'Shiny Gems','✨💎',40,30)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.cheese_jumpers
    Jitems.newItem(access,'Cheese JumperS','🧀🥋',90,100)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.blue_cheese
    Jitems.newItem(access,'Blue Cheese','Ƀ🧀',90,150)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.pebbles
    Jitems.newItem(access,'Pebbles','⭖',2,5)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.sticks
    Jitems.newItem(access,'Sticks','/',5,10)
    return