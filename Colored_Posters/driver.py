from main import main
lines=open('./images.in').read().splitlines()

for i,line in enumerate(lines):
    main(f'output{i}.png',line)
    
