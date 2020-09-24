# cookbook-app
## Django Framework Studies (pt-BR)

This project is part of my Djando Framework Study.
It consists in a Cook Book web-app, where is possible do add, edit and search for cooki receipts.
All posts are stored into a PostGreSQL Database, that runs over a docker conteiner
All Django environment was virtualized using conda

##ToDO
- Dockerize Conda Environment
- Create conda environment if it don't exists during container execution
- Activate Conda Environment if it already exists or after its creation
- Run Djando static and migration commands during container start
- Run Django runserver 
