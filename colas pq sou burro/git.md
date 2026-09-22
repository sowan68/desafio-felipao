##### **autoexplicativo, mas eu sou burro, então são os dados da sua conta do GitHub, estupido bastardo**



git config --global user.name "sowan68"

git config --global user.email "ezequieltenoriopereira@gmail.com"



##### **crendential helper é pra guardar sua senha, quando tu coloca uma vez ele não pede mais**



git config --global crendential.helper store 



##### **é o comando que transforma uma pasta comum em um repositório Git ;)**



git init



###### **prepara as alterações para serem incluídas no próximo commit, não salva definitivamente ainda. tu tá tipo falando pro Git: "quero incluir essas alterações no próximo commit.**



git add (nome dos arquivos)// git add . (para adicionar todos os arquivos)



##### **cria um registro das alterações no seu computador, -m serve para mensagem**



git commit -m "first commit"



##### **serve pra você renomear o nome da branch (ou caixinha) q vc tá**



git branch -M main



##### **aq é pra vc linkar o seu repositório com o seu pc, ou seja, pra onde vc quer comunicar os arquivos.**



git remote add origin https://github.com/sowan68/desafio-felipao2.git



##### **o git vai puxar tudo que tem da tua máquina pra mandar pro GitHub, ou seja envia os commits que estão no seu computador para o repositório remoto, o bucetudo do GitHub.**



git push -u origin main



