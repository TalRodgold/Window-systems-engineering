from bot import bot
def main():
    b=bot("lev",40)
    b.send("Israel will win")
    b.send("Israel is winning "*2)
    b.send("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Fusce ac facilisis mauris, in lacinia ante. Sed sit amet nisl ante.
    Pellentesque ut eleifend sem. Nulla eleifend neque non """)

if __name__=="__main__":
 main()