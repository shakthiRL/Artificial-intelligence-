def print_board(b):
 for r in b:
  print("|".join(r),"\n-----")


def check(b, p):
 for r in b+[c for c in zip(*b)]+[[b[i][i]for i in range(3)],[b[i][2-i]for i in range(3)]]:
  if len(set(r))==1and r[0]==p:return 1


def tic_tac_toe():
 b=[[" "]*3 for _ in range(3)]
 p,i=["X","O"],0
 while 1:
  print_board(b)
  r,c=map(int,input(f"Player {p[i%2]}'s turn.\nEnter row and column (0-2): ").split())
  if b[r][c]==" ":
   b[r][c]=p[i%2]
   if check(b,p[i%2]):print_board(b);print(f"Player {p[i%2]} wins!");break
   if all(" "not in r for r in b):print_board(b);print("It's a tie!");break
   i+=1
  else:print("That spot is already taken. Try again.")


if __name__ == "__main__":
    tic_tac_toe()
