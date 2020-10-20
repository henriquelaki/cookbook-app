# cookbook-app

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a0ab4fa39c474c5a9a038499c0e3e46d)](https://app.codacy.com/manual/henrique.laki/cookbook-app?utm_source=github.com&utm_medium=referral&utm_content=henriquelaki/cookbook-app&utm_campaign=Badge_Grade_Settings)

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
