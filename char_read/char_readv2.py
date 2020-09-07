import discord
import os

def find_trait(t):

    traits = ["-Name:", "-Age :", "-Desc:", "-Reas:", "-Posi:", "-Chan:"]
    
    for i in range(len(traits)):
        if t.find(traits[i]) != -1:
            return i

    return -1

def collect_traits(c_file):

    char_lines = c_file.readlines()

    traits = []
    trait_names = ["Name", "Age", "Description", "Reason to Climb", "Position", "Channel"]
    i = -1
    for text in char_lines:
        
        ns = text.find("\n")
        if ns != -1:
            text = text[:text.find("\n")]
        
        trait = find_trait(text)
        if trait != -1:
            traits.append([trait_names[trait],text[7:]])
            i += 1
        else:
            traits[i][1] += " " + text

    return traits

def build_emb(traits):

    emb = discord.Embed(title = traits[0][1])
    
    for i in range(len(traits) - 2):
        emb.add_field(name = traits[i+1][0], value = traits[i+1][1], inline = False)
    
    return emb
    

def collect_char_embs():

    char_embs = []
    char_chans = []
    char_files = []

    for c_file in os.listdir(".\\tog_chars"):
        if c_file.endswith(".txt"):
            char_file = open(os.path.join(".\\tog_chars", c_file), "r")
            traits = collect_traits(char_file)
            char_embs.append(build_emb(traits))
            char_chans.append(traits[len(traits)-1][1])
            char_files.append(c_file)
    
    return char_embs, char_chans, char_files