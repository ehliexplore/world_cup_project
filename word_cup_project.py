from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk


def brazil_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Brazil

     Matches 

     Brazil x Serbia 
     2           0

     Brazil x Switzerland
     1            0

     Brazil x Cameroon
     0             1

     Brazil x South Korea
     4             1

     Brazil x Croatia
     1 (2)             1 (4)
     """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=brazil_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def brazil_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Brazil squad

Goalkeepers: 
Alisson, Ederson, Weverton.

Defenders: 
Dani Alves, Danilo, Alex Sandro, Alex Telles, 
Bremer, Eder Militao, Marquinhos, Thiago Silva.

Midfielders: 
Bruno Guimaraes, Casemiro, Everton Ribeiro, 
Fabinho, Fred, Lucas Paqueta.

Forwards: 
Antony, Gabriel Jesus, Gabriel Martinelli, Neymar, Pedro, 
Raphinha, Richarlison, Rodrygo, Vinicius Junior.""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=brazil_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def portugal_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Portugal
    
    Matches
    
    Portugal x Ghana
    3           2
    
    Portugal x Uruguay
    2           0
    
    Portugal x South Korea
    2           1
    
    Portugal x Switzerland
    6           1
    
    Portugal x Morocco
    0           1
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=portugal_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def portugal_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Portugal squad
    
    Goalkeepers: 
    Jose Sa, Rui Patricio, Diogo Costa.
    
Defenders: 
Joao Cancelo, Diogo Dalot, Pepe, Ruben Dias, Danilo Pereira, 
Antonio Silva, Nuno Mendes, Raphael Guerreiro.

Midfielders: 
William, Ruben Neves, Joao Palhinha, Bruno Fernandes, 
Vitinha, Otavio, Matheus Nunes, Bernardo Silva, Joao Mario.

Forwards: 
Cristiano Ronaldo, Joao Felix, Rafael Leao, Ricardo Horta, 
Andre Silva, Goncalo Ramos.""", font=('Arial', 14))
    players_lb.place(relx=0.1, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=portugal_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def argentina_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Argentina
    
    Matches
    
    Argentina x Saudi Arabia
    1           2
    
    Argentina x Mexico
    2           0
    
    Argentina x Poland
    2           0
    
    Argentina x Australia
    2           1
    
    Argentina x Netherlands
    2 (4) x     2 (3)
    
    Argentina x Croatia
    3           0

    Argentina x France 
    3 (4)       3 (2)""", font=('Arial', 15))
    lb.place(relx=0.3, rely=0.01)

    back = ttk.Button(frame_right, text='Back', command=argentina_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def argentina_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Argentina squad

Goalkeepers: 
Emiliano Martinez, Geronimo Rulli, Franco Armani

Defenders: 
Nahuel Molina, Gonzalo Montiel, Cristian Romero, German Pezzella, 
Nicolas Otamendi, Lisandro Martinez, 
Marcos Acuna, Nicolas Tagliafico, Juan Foyth.

Midfielders: 
Rodrigo De Paul, Leandro Paredes, Alexis Mac Allister, 
Guido Rodriguez, Alejandro Gomez, 
Enzo Fernandez, Exequiel Palacios.

Forwards: 
Angel Di Maria, Paulo Dybala, Lautaro Martinez, Julian Alvarez, 
Nicolas Gonzalez, Joaquin Correa, Lionel Messi.""", font=('Arial', 14))
    players_lb.place(relx=0.08, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=argentina_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def senegal_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Senegal
    
    Matches
    
    Senegal x Netherlands
    0           2
    
    Senegal x Qatar
    3           1
    
    Senegal x  Ecuador
    2           1
    
    Senegal x England
    0           3""", font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=senegal_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def senegal_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Senegal squad

Goalkeepers: 
Edouard Mendy, Alfred Gomis, Seny Diang.

Defenders: 
Bouna Sarr, Saliou Ciss, Kalidou Koulibaly, Pape Abou Cisse, 
Abdou Diallo, Ibrahima Mbaye, 
Abdoulaye Seck, Fode Ballo Toure, Cheikhou Kouyate.

Midfielders: 
Pape Matar Sarr, Pape Gueye, Nampalys Mendy, Idrissa Gana Gueye, 
Moustapha Name, M. Loum Ndiaye, Joseph Lopy.

Forwards: 
Sadio Mane, Ismaila Sarr, Bamba Dieng, Keita Balde, Habib Diallo, 
Boulaye Dia, Famara Diedhiou, Mame Babe Thiam.""", font=('Arial', 14))
    players_lb.place(relx=0.05, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=senegal_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def spain_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Spain
    
    Matches
    
    Spain x Costa Rica
    7           0
    
    Spain x Germany
    1           1
    
    Spain x Japan
    2           1
    
    Spain x Morocco
    0 (0)       0 (3)""", font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=spain_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def spain_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Spain squad

Goalkeepers: 
Unai Simón, Robert Sánchez, David Raya.

Defenders: 
Dani Carvajal, César Azpilicueta, Eric García, 
Hugo Guillamón, Pau Torres, Laporte, Jordi Alba, Jose Gayá.

Midfielders: 
Sergio Busquets, Rodri, Gavi, 
Carlos Soler, Marcos Llorente, Pedri, Koke.

Forwards: 
Ferran Torres, Pablo Sarabia, Yeremy Pino, Alvaro Morata, 
Marco Asensio, Nico Williams, Ansu Fati, Dani Olmo.""", font=('Arial', 14))
    players_lb.place(relx=0.1, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=spain_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def iran_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Iran 
    
    Matches
    
    Iran x England
    2           6
    
    Iran x Wales
    2           0
    
    Iran x EUA
    0           1
    """, font=('Arial', 15))
    lb.place(relx=0.35, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=iran_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def iran_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Iran squad

Goalkeepers: 
Alireza Beiranvand, Amir Abedzadeh, 
Hossein Hosseini, Payam Niazmand.

Defenders: 
Ehsan Hajsafi, Morteza Pouraliganji, Ramin Rezaeian, Milad Mohammadi, 
Hossein Kanani, Shojae Khalilzadeh, Sadegh Moharrami, 
Rouzbeh Cheshmi, Majid Hosseini, Abolfazl Jalali.

Midfielders: 
Ahmad Noorollahi, Saman Ghoddos, Vahid Amiri, Saeid Ezatolahi, 
Alireza Jahanbakhsh, Mehdi Torabi, Ali Gholizadeh, Ali Karimi.

Forwards: 
Karim Ansarifard, Sardar Azmoun, Mehdi Taremi.""", font=('Arial', 14))
    players_lb.place(relx=0.05, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=iran_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def usa_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    EUA
    
    Matches
    
    EUA x Wales
    1           1
    
    EUA x England
    0           0
    
    EUA x Iran
    1           0
    
    EUA x Netherlands
    1           3
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=usa_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def usa_players():
    clean_frame()
    players_lb = Label(frame_right, text="""USA squad

Goalkeepers: 
Ethan Horvath, Matt Turner, Sean Johnson.

Defenders: 
Joe Scally, Sergino Dest, Cameron Carter-Vickers, 
Aaron Long, Walker Zimmerman, Shaq Moore, 
DeAndre Yedlin, Tim Ream, Antonee Robinson.

Midfielders: 
Cristian Roldan, Kellyn Acosta, Luca de la Torre, 
Yunus Musah, Weston McKennie, 
Tyler Adams, Brenden Aaronson.

Forwards: 
Jordan Morris, Jesus Ferreira, Christian Pulisic, Josh Sargent, 
Giovanni Reyna, Timothy Weah, Haji Wright.""", font=('Arial', 14))
    players_lb.place(relx=0.05, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=usa_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def japan_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Japan
    
    Matches
    
    Japan x Germany
    2           1
    
    Japan x Costa Rica
    0           1
    
    Japan x Spain
    2           1
    
    Japan x Croatia
    1 (1)       1 (3)""", font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=japan_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def japan_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Japan squad

Goalkeepers: 
Shuichi Gonda, Daniel Schmidt, Eiji Kawashima.

Defenders: 
Miki Yamane, Hiroki Sakai, 
Maya Yoshida, Takehiro Tomiyasu, 
Shogo Taniguchi, Ko Itakura, Hiroki Ito, Yuto Nagatomo.

Midfielders: 
Wataru Endo, Hidemasa Morita, 
Ao Tanaka, Gaku Shibasaki, Kaoru Mitoma, 
Daichi Kamada, Ritsu Doan, Junya Ito, 
Takumi Minamino, Takefusa Kubo, Yuki Soma.

Forwards: 
Daizen Maeda, Takuma Asano, 
Shuto Machino, Ayase Ueda.""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=japan_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def france_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    France
    
    Matches
    
    France x Australia
    4           1
    
    France x Denmark
    2           1
    
    France x Tunisia
    0           1
    
    France x Poland
    2           1
    
    France x England
    2           1
    
    France x Morocco
    2           0
    
    France x Argentina
    3 (2)       3 (4)
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.01)

    back = ttk.Button(frame_right, text='Back', command=france_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def france_players():
    clean_frame()
    players_lb = Label(frame_right, text="""France squad

Goalkeepers: 
Hugo Lloris, Alphonse Areola, Steve Mandanda.

Defenders: 
Benjamin Pavard, Jules Koundé, Raphael Varane, 
Presnel Kimpembe, William Saliba, Lucas Hernandez, 
Theo Hernandez, Ibrahima Konaté, Dayot Upamecano.

Midfielders: 
Adrien Rabiot, Aurelien Tchouaméni, 
Youssouf Fofana, Matteo Guendouzi, 
Jordan Veretout, Eduardo Camavinga.

Forwards: 
Kingsley Coman, Kylian Mbappé, 
Karim Benzema, Olivier Giroud, 
Antoine Griezmann, Ousmane Dembélé, Christophe Nkunku.""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=france_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def germany_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Germany
    
    Matches
    
    Germany x Japan
    1           2
    
    Germany x Spain
    1           1
    
    Germany x Costa Rica
    4           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=germany_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def germany_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Germany squad

Goalkeepers: 
Manuel Neuer, Marc-Andre ter Stegen, Kevin Trapp.

Defenders: 
Armel Bella-Kotchap, Matthias Ginter, Christian Günter, 
Thilo Kehrer, Lukas Klostermann, David Raum, 
Antonio Rudiger, Nico Schlotterbeck, Niklas Süle

Midfielders: 
Julian Brandt, Niklas Füllkrug, Leon Goretzka, 
Mario Götze, Ilkay Gundogan, 
Jonas Hofmann, Joshua Kimmich, Jamal Musiala

Forwards: 
Karim Adeyemi, Serge Gnabry, Kai Havertz, 
Youssoufa Moukoko, Thomas Müller, Leroy Sané.
""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=germany_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def tunisia_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Tunisia
    
    Matches
    
    Tunisia x Denmark
    0           0
    
    Tunisia x Australia
    0           1
    
    Tunisia x France
    1           0
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=tunisia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def tunisia_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Tunisia squad

Goalkeepers: 
Aymen Dahmen, Bechir Ben Said, 
Mouez Hassen, Aymen Mathlouthi

Defenders: 
Ali Abdi, Dylan Bronn, Mohamed Drager, 
Nader Ghandri, Bilel Ifa, Wajdi Kechrida, 
Ali Maaloul, Yassine Meriah, Montassar Talbi

Midfielders: 
Mohamed Ali Ben Romdhane, Ghaylane Chaalali, 
Aissa Laidouni, Hannibal Mejbri, 
Ferjani Sassi, Elyas Skhiri

Forwards: 
Anis Ben Slimane, Seifeddine Jaziri, 
Issam Jebali, Wahbi Khazri, Taha Yassine Khenissi, 
Youssef Msakni, Naim Sliti
""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=tunisia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def costa_rica_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Costa Rica
    
    Matches
    
    Costa Rica x Spain
    0               7
    
    Costa Rica x Japan
    1               0
    
    Costa Rica x Germany
    2               4
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=costa_rica_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def costa_rica_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Costa Rica squad

Goalkeepers: 
Keylor Navas, Esteban Alvarado, Patrick Sequeira.

Defenders: 
Francisco Calvo, Juan Pablo Vargas, 
Kendall Waston, Oscar Duarte, Daniel Chacon, 
Keysher Fuller, Carlos Martinez, 
Bryan Oviedo, Ronald Matarrita.

Midfielders: 
Yeltsin Tejeda, Celso Borges, Youstin Salas, Roan Wilson, 
Gerson Torres, Douglas Lopez, Jewison Bennette, 
Alvaro Zamora, Anthony Hernandez, 
Brandon Aguilera, Bryan Ruiz.

Forwards: 
Joel Campbell, Anthony Contreras, 
Johan Venegas.
""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=costa_rica_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def australia_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Australia
    
    Matches
    
    Australia x France
    1           4
    
    Australia x Tunisia
    1           0
    
    Australia x Denmark
    1           0
    
    Australia x Argentina
    1           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=australia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def australia_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Australia squad

Goalkeepers: 
Maty Ryan, Andrew Redmayne, Danny Vukovic

Defenders: 
Milos Degenek, Aziz Behich, Joel King, 
Nathaniel Atkinson, Fran Karacic, Harry Souttar, 
Kye Rowles, Bailey Wright, Thomas Deng

Midfielders: 
Aaron Mooy, Jackson Irvine, Ajdin Hrustic, 
Keanu Baccus, Cameron Devlin, Riley McGree

Forwards: 
Awer Mabil, Mathew Leckie, Martin Boyle, 
Jamie Maclaren, Jason Cummings, Mitchell Duke, 
Garang Kuol, Craig Goodwin
""", font=('Arial', 14))
    players_lb.place(relx=0.17, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=australia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def netherlands_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Netherlands
    
    Matches
    
    Netherlands x Senegal
    2               0
    
    Netherlands x Ecuador
    1               1
    
    Netherlands x Qatar
    2               0
    
    Netherlands x USA
    3               1
    
    Netherlands x Argentina
    2 (3)           2 (4)
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=netherlands_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def netherlands_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Netherlands squad

Goalkeepers: 
Justin Bijlow, Andries Noppert, Remko Pasveer.

Defenders: 
Virgil van Dijk, Nathan Ake, Daley Blind, Jurrien Timber, 
Denzel Dumfries, Stefan de Vrij, Matthijs de Ligt, 
Tyrell Malacia, Jeremie Frimpong.

Midfielders: 
Frenkie de Jong, Steven Berghuis, 
Davy Klaassen, Teun Koopmeiners, Cody Gakpo, 
Maarten de Roon, Kenneth Taylor, Xavi Simons.

Forwards: 
Memphis Depay, Steven Bergwijn, 
Vincent Janssen, Luuk de Jong, Noa Lang, 
Wout Weghorst.
""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=netherlands_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def morocco_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Morocco
    
    Matches
    
    Morocco x Croatia
    0           0
    
    Morocco x Belgium
    2           0
    
    Morocco x Canada
    1           2
    
    Morocco x Spain
    0 (3)       0 (0)
    
    Morocco x Portugal
    1           0
    
    Morocco x Croatia
    1           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=morocco_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def morocco_players():
    clean_frame()
    players_lb = Label(frame_right, text="""Morocco squad

Goalkeepers: 
Yassine Bono, Munir, Ahmed Reda Tagnaouti.

Defenders: 
Achraf Hakimi, Romain Saiss, Noussair Mazraoui, 
Nayef Aguerd, Achraf Dari, Jawad El-Yamiq, 
Yahia Attiat-Allal, Badr Benoun.

Midfielders: 
Sofyan Amrabat, Selim Amallah, Abdelhamid Sabiri, 
Azzedine Ounahi, Bilel El Khanouss, Yahya Jabrane.

Forwards: 
Hakim Ziyech, Youssef El-Nesri, 
Sofiane Boufal, Ez Abde, 
Amine Harit, Zakaria Aboukhlal, 
Ilias Chair, Walid Cheddira, 
Abderazzak Hamdallah.
""", font=('Arial', 14))
    players_lb.place(relx=0.12, rely=0.2)

    back = ttk.Button(frame_right, text='Back', command=morocco_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def serbia_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Serbia
    
    Matches
    
    Serbia x Brazil
    0           2
    
    Serbia x Cameroon
    3           3
    
    Serbia x Switzerland
    2           3""", font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=serbia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def serbia_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
    Serbia squad

Goalkeepers: 
Marko Dmitrovic, Pedrag Rajkovic, 
Vanja Milinkovic Savic.

Defenders: 
Stefan Mitrovic, Nikola Milenkovic, Strahinja Pavlovic, 
Milos Veljkovic, Filip Mladenovic, 
Strahinja Erakovic, Srdan Babic.

Midfielders: 
Nemanja Gudelj, Sergej Milinkovic Savic, Sasa Lukic, Marko Grujic, 
Filip Kostic, Uros Racic, 
Nemanja Maksimovic, Ivan Ilic, Andrija Zivkovic, Darko Lazovic.

Forwards: 
Dusan Tadic, Aleksandar Mitrovic, 
Dusan Vlahovic, Filip Duricic, Luka Jovic, 
Nemanja Radonjic.
""", font=('Arial', 14))
    players_lb.place(relx=0.1, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=serbia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def uruguay_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Uruguay
    
    Matches
    
    Uruguay x South Korea
    0           0
    
    Uruguay x Portugal
    0           2
    
    Uruguay x Ghana
    2           0
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=serbia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def uruguay_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
    Uruguay squad

Goalkeepers: 
Fernando Muslera, Sergio Rochet, Sebastian Sosa

Defenders: 
Diego Godin, Jose Maria Gimenez, Ronald Araujo, 
Sebastian Coates, Martin Caceres, Mathias Olivera, 
Matias Vina, Guillermo Varela, Josa Luis Rodríguez.

Midfielders: 
Manuel Ugarte, Federico Valverde, Rodrigo Bentancur, 
Matias Vecino, Lucas Torreira, 
Nico de la Cruz, Giorgian de Arrascaeta.

Forwards: 
Luis Suarez, Edinson Cavani, Darwin Nunez, 
Maxi Gomez, Facundo Pellistri, 
Agustin Canobbio, Facundo Torres.
""", font=('Arial', 14))
    players_lb.place(relx=0.1, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=uruguay_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def wales_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Wales
    
    Matches
    
    Wales x USA
    1           1
    
    Wales x Iran
    0           2
    
    Wales x England
    0           3
    """, font=('Arial', 15))
    lb.place(relx=0.35, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=wales_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def wales_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
    Wales squad

Goalkeepers: 
Wayne Hennessey, Danny Ward, Adam Davies.

Defenders: 
Ben Davies, Ben Cabango, Tom Lockyer, 
Joe Rodon, Chris Mepham, Ethan Ampadu, 
Chris Gunter, Neco Williams, Connor Roberts.

Midfielders: 
Sorba Thomas, Joe Allen, Matthew Smith, 
Dylan Levitt, Harry Wilson, Joe Morrell, 
Jonny Williams, Aaron Ramsey, Rubin Colwill.

Forwards: 
Gareth Bale, Kieffer Moore, 
Mark Harris, Brennan Johnson, Dan James.
""", font=('Arial', 14))
    players_lb.place(relx=0.2, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=wales_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def south_korea_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    South Korea
    
    Matches
    
    South Korea x Uruguay
    0               0
    
    South Korea x Ghana
    2               3
    
    South Korea x Portugal
    2               1
    
    South Korea x Brazil
    1               4
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=south_korea_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def south_korea_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Korea squad

Goalkeepers: 
Kim Seung-gyu, Jo Hyeon-woo, Song Bum-keun

Defenders: 
Kim Min-jae, Kim Jin-su, Hong Chul, 
Kim Moon-hwan, Yoon Jong-gyu, Kim Young-gwon, 
Kim Tae-hwan, Kwon Kyung-won, Cho Yu-min

Midfielders: 
Jung Woo-young, Na Sang-ho, 
Paik Seung-ho, Son Jun-ho, Song Min-kyu, 
Kwon Chang-hoon, Lee Jae-sung, Hwang Hee-chan, 
Hwang In-beom, Jeong Woo-yeong, Lee Kang-in

Forwards: 
Hwang Ui-jo, Cho Gue-sung, Son Heung-min
""", font=('Arial', 14))
    players_lb.place(relx=0.2, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=south_korea_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def switzerland_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Switzerland
    
    Matches
    
    Switzerland  x Cameroon
    1               0
    
    Switzerland x Brazil
    0               1
    
    Switzerland x Serbia
    3               2
    
    Switzerland x Portugal
    1               6
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=switzerland_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def switzerland_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Switzerland squad

Goalkeepers: 
Gregor Kobel, Yann Sommer, Jonas Omlin, Philipp Kohn.

Defenders: 
Manuel Akanji, Eray Comert, 
Nico Elvedi, Fabian Schar, Silvan Widmer, 
Ricardo Rodriguez, Edimilson Fernandes.

Midfielders: 
Michel Aebischer, Xherdan Shaqiri, 
Renato Steffen, Granit Xhaka, Denis Zakaria, 
Fabian Frei, Remo Freuler, Noah Okafor, 
Fabian Rieder, Ardon Jashari.

Forwards: Breel Embolo, Ruben Vargas, 
,
Djibril Sow, Haris Seferovic, Christian Fassnacht.
""", font=('Arial', 14))
    players_lb.place(relx=0.1, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=switzerland_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def denmark_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Denmark
    
    Matches
    
    Denmark x Tunisia
    0           0
    
    Denmark x France
    1           2
    
    Denmark x Australia
    0           1
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=denmark_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def denmark_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Denmark squad

Goalkeepers: 
Kasper Schmeichel, Oliver Christensen, Frederik Ronnow

Defenders: 
Simon Kjaer, Joachim Andersen, Joakim Maehle, 
Andreas Christensen, Rasmus Kristensen, 
Jens Stryger Larsen, Victor Nelsson, 
Daniel Wass, Alexander Bah

Midfielders: 
Thomas Delaney, Mathias Jensen, Christian Eriksen, 
Pierre-Emile Hojbjerg, Christian Norgaard

Forwards: 
Andreas Skov Olsen, Jesper Lindstrom, Andreas Cornelius, 
Martin Braithwaite, Kasper Dolberg, Mikkel Damsgaard, 
Jonas Wind, Robert Skov, Yussuf Poulsen
""", font=('Arial', 14))
    players_lb.place(relx=0.1, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=denmark_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def ghana_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Ghana 
    
    Matches
    
    Ghana x Portugal
    2           3
    
    Ghana x South Korea
    3           2
    
    Ghana x Uruguay
    0           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=ghana_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def ghana_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Ghana squad

Goalkeepers: 
Lawrence Ati, Danlad Ibrahim, Manaf Nurudeen

Defenders: 
Joseph Aidoo, Daniel Amartey, Baba Rahman, 
Alexander Djiku, Tariq Lamptey, Gideon Mensah, 
Denis Odoi, Mohammed Salisu, Alidu Seidu

Midfielders: 
Andre Ayew, Mohammed Kudus, Daniel-Kofi Kyereh, 
Elisha Owusu, Thomas Partey, Salis Abdul Samed

Forwards: 
Daniel Afriyie, Jordan Ayew, Osman Bukari, 
Issahaku Abdul Fatawu, Antoine Semenyo, 
Kamal Sowah, Kamaldeen Sulemana, Inaki Williams
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=ghana_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def ecuador_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Ecuador
    
    Matches
    
    Ecuador x Qatar
    2           0
    
    Ecuador x Netherlands
    1           1
    
    Ecuador x Senegal
    1           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=ecuador_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def ecuador_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Ecuador squad

Goalkeepers: 
Moises Ramirez, Alexander Dominguez, 
Hernan Galindez

Defenders: 
Piero Hincapie, Robert Arboleda, 
Pervis Estupinan, Angelo Preciado, 
Jackson Porozo, Xavier Arreaga, 
Felix Torres, Diego Palacios, William Pacho

Midfielders: 
Carlos Gruezo, Jose Cifuentes, Alan Franco, 
Moises Caicedo, Angel Mena, Jeremy Sarmiento, 
Ayrton Preciado, Sebastian Mendez, 
Gonzalo Plata, Romario Ibarra

Forwards: 
Djorkaeff Reasco, Kevin Rodriguez, 
Michael Estrada, Enner Valencia
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=ecuador_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def canada_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Canada
    
    Matches
    
    Canada x Belgium
    0           1
    
    Canada x Croatia
    1           4
    
    Canada x Morocco
    1           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=canada_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def canada_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Canada squad

Goalkeepers: 
James Pantemis, Milan Borjan, Dayne St Clair

Defenders: 
Samuel Adekugbe, Joel Waterman, 
Alistair Johnston, Richie Laryea, 
Kamal Miller, Steven Vitoria, Derek Cornelius

Midfielders: 
Liam Fraser, Ismael Kone, Mark-Anthony Kaye, 
David Wotherspoon, Jonathan Osorio, 
Atiba Hutchinson, Stephen Eustaquio, Samuel Piette

Forwards: 
Tajon Buchanan, Liam Millar, Lucas Cavallini, 
Ike Ugbo, Junior Hoilett, Jonathan David, 
Cyle Larin, Alphonso Davies
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=canada_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def mexico_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Mexico 
    
    Matches
    
    Mexico x Poland
    0           0
    
    Mexico x Argentina
    0           2
    
    Mexico x Saudi Arabia
    2           1
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=mexico_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def mexico_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Mexico squad

Goalkeepers: 
Guillermo Ochoa, Alfredo Talavera, Rodolfo Cota

Defenders: 
Kevin Alvarez, Nestor Araujo, Gerardo Arteaga, 
Jesus Gallardo, Hector Moreno, Cesar Montes, 
Jorge Sanchez, Johan Vasquez

Midfielders: 
Edson Alvarez, Roberto Alvarado, 
Uriel Antuna, Luis Chavez, Andres Guardado, 
Erick Gutierrez, Hector Herrera, Orbelin Pineda, 
Carlos Rodriguez, Luis Romo

Forwards: 
Rogelio Funes Mori, Raul Jimenez, 
Hirving Lozano , Henry Martin, Alexis Vega
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=mexico_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def cameroon_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Cameroon
    
    Matches
    
    Cameroon x Switzerland
    0           1
    
    Cameroon x Serbia
    3           3
    
    Cameroon x Brazil
    1           0
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=cameroon_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def cameroon_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Cameroon squad

Goalkeepers: 
Devis Epassy, Simon Ngapandouetnbu, Andre Onana.

Defenders: 
Jean-Charles Castelletto, Enzo Ebosse, 
Collins Fai, Olivier Mbaizo, Nicolas Nkoulou, 
Tolo Nouhou, Christopher Wooh.

Midfielders: 
Martin Hongla, Pierre Kunde, Olivier Ntcham, 
Gael Ondoua, Samuel Oum Gouet, 
Andre-Frank Zambo Anguissa.

Forwards: 
Vincent Aboubakar, Christian Bassogog, 
Eric-Maxime Choupo Moting, Souaibou Marou, 
Bryan Mbeumo, Nicolas Moumi Ngamaleu, 
Jerome Ngom, Georges-Kevin Nkoudou, 
Jean-Pierre Nsame, Karl Toko Ekambi.
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=cameroon_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def belgium_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Belgium
    
    Matches
    
    Belgium x Canada
    1           0
    
    Belgium x Morocco
    0           2
    
    Belgium x Croatia
    0           0
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=belgium_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def belgium_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Belgium squad

Goalkeepers: 
Thibaut Courtois, Simon Mignolet, Koen Casteels.

Defenders: 
Jan Vertonghen, Toby Alderweireld, 
Leander Dendoncker, Wout Faes, Arthur Theate, 
Zeno Debast, Yannick Carrasco, Thomas Meunier, 
Timothy Castagne, Thorgan Hazard.

Midfielders: 
Kevin de Bruyne, Youri Tielemans, 
Andre Onana, Axel Witsel, Hans Vanaken.

Forwards: 
Eden Hazard, Charles De Ketelaere, 
Leandro Trossard, Dries Mertens, Jeremy Doku, 
Romelu Lukaku, Michy Batshuayi, Lois Openda.
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=belgium_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def qatar_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Qatar
    
    Matches
    
    Qatar x Ecuador
    0           2
    
    Qatar x Senegal
    1           3
    
    Qatar x Netherlands
    0           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=qatar_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def qatar_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Qatar squad

Goalkeepers: 
Saad Al-Sheeb, Meshaal Barsham, Yousef Hassan

Defenders: 
Pedro Miguel, Musaab Khidir, Tarek Salman, 
Bassam Al-Rawi, Boualem Khoukhi, 
Abdelkarim Hassan, Homam Ahmed, Jassem Gaber

Midfielders: 
Ali Asad, Assim Madabo, Mohammed Waad, 
Salem Al-Hajri, Moustafa Tarek, 
Karim Boudiaf, Abdelaziz Hatim, Ismail Mohamad

Forwards: 
Naif Al-Hadhrami, Ahmed Alaaeldin, 
Hassan Al-Haydos, Khalid Muneer, 
Akram Afif, Almoez Ali, Mohamed Muntari
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=qatar_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def england_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    England
    
    Matches
    
    England x Iran
    6           2
    
    England x USA
    0           0
    
    England x Wales
    3           0
    
    England x Senegal
    3           0
    
    England x France
    1           2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=england_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def england_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
England squad

Goalkeepers: 
Jordan Pickford, Nick Pope, Aaron Ramsdale.

Defenders: 
Harry Maguire, John Stones, Kyle Walker, 
Luke Shaw, Kieran Trippier, Trent Alexander-Arnold, 
Eric Dier, Conor Coady, Ben White.

Midfielders: 
Declan Rice, Jude Bellingham, 
Jordan Henderson, Mason Mount, 
Kalvin Phillips, James Maddison, 
Conor Gallagher.

Forwards: 
Harry Kane, Phil Foden, Raheem Sterling, 
Marcus Rashford, Bukayo Saka, 
Jack Grealish, Callum Wilson.
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=england_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def poland_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Poland
    
    Matches
    
    Poland x Mexico
    0           0
    
    Poland x Saudi Arabia
    2           0
    
    Poland x Argentina
    0           2
    
    Poland x France
    1           3
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=poland_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def poland_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Poland squad

Goalkeepers: 
Wojciech Szczesny, Bartlomiej Dragowski, 
Lukasz Skorupski.

Defenders: 
Jan Bednarek, Kamil Glik, Robert Gumny, 
Artur Jedrzejczyk, Jakub Kiwior, 
Mateusz Wieteska, Bartosz Bereszynski, 
Matty Cash, Nicola Zalewski.

Midfielders: 
Krystian Bielik, Przemyslaw Frankowski, 
Kamil Grosicki, Grzegorz Krychowiak, Jakub Kaminski, 
Michal Skoras, Damian Szymanski, Sebastian Szymanski, 
Piotr Zielinski, Szymon Zurkowski.

Forwards: Robert Lewandowski, 
Arkadiusz Milik, Krzysztof 
Piatek, Karol Swiderski.
""", font=('Arial', 14))
    players_lb.place(relx=0.15, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=poland_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def saudi_arabia_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Saudi Arabia
    
    Matches
    
    Saudi Arabia x Argentina
    2               1
    
    Saudi Arabia x Poland
    0               2
    
    Saudi Arabia x Mexico
    1               2
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=saudi_arabia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def saudi_arabia_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Saudi Arabia squad

Goalkeepers: 
Mohamed Al-Owais, Nawaf Al-Aqidi, 
Mohamed Al-Yami

Defenders: 
Yasser Al-Shahrani, Ali Al-Bulaihi, 
Abdulelah Al-Amri, Abdullah Madu, 
Hassan Tambakti, Sultan Al-Ghanam, 
Mohammed Al-Breik, Saud Abdulhamid

Midfielders: 
Salman Al-Faraj, Riyadh Sharahili, 
Ali Al-Hassan, Mohamed Kanno, 
Abdulelah Al-Malki, Sami Al-Najei, 
Abdullah Otayf, Nasser Al-Dawsari , 
Abdulrahman Al-Aboud, 
Salem Al-Dawsari, Hattan Bahebri

Forwards: 
Haitham Asiri, Saleh Al-Shehri, 
Firas Al-Buraikan
""", font=('Arial', 14))
    players_lb.place(relx=0.22, rely=0.07)

    back = ttk.Button(frame_right, text='Back', command=saudi_arabia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def croatia_matches():
    clean_frame()
    lb = Label(frame_right, text="""
    Croatia
    
    Matches
    
    Croatia x Canada
    4           1
    
    Croatia x Belgium
    0           0
    
    Croatia x Japan
    1 (3)       1 (1)
    
    Croatia x Brazil
    1 (4)       1 (2)
    
    Croatia x Argentina
    0           3
    
    Croatia x Morocco
    2           1
    """, font=('Arial', 15))
    lb.place(relx=0.3, rely=0.1)

    back = ttk.Button(frame_right, text='Back', command=croatia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def croatia_players():
    clean_frame()
    players_lb = Label(frame_right, text="""
Croatia squad

Goalkeepers: 
Dominik Livakovic, Ivica Ivusic, Ivo Grbic

Defenders: Domagoj Vida, Dejan Lovren, 
Borna Barisic, Josip Juranovic, Josko Gvardiol, 
Borna Sosa, Josip Stanisic, Martin Erlic, 
Josip Sutalo

Midfielders: Luka Modric, Mateo Kovacic, 
Marcelo Brozovic, Mario Pasalic, Nikola Vlasic, 
Lovro Majer, Kristijan Jakic, Luka Sucic

Forwards: Ivan Perisic, Andrej Kramaric, 
Bruno Petkovic, Mislav Orsic, Ante Budimir, 
Marko Livaja
""", font=('Arial', 14))
    players_lb.place(relx=0.22, rely=0.07)

    back = ttk.Button(frame_right, text='Back', command=croatia_options)
    back.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.05)


def brazil_options():
    clean_frame()

    name = Label(frame_right, text='Brazil', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=brazil_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=brazil_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def portugal_options():
    clean_frame()

    name = Label(frame_right, text='Portugal', font=('Arial', 20))
    name.place(relx=0.43, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=portugal_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=portugal_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def argentina_options():
    clean_frame()

    name = Label(frame_right, text='Argentina', font=('Arial', 20))
    name.place(relx=0.43, rely=0.2)

    winner = Label(frame_right, text='Winner of Worldcup 2022', font=('arial', 20))
    winner.place(relx=0.3, rely=0.3)

    matches = ttk.Button(frame_right, text='Matches', command=argentina_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=argentina_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def senegal_options():
    clean_frame()

    name = Label(frame_right, text='Senegal', font=('Arial', 20))
    name.place(relx=0.43, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=senegal_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=senegal_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def spain_options():
    clean_frame()

    name = Label(frame_right, text='Spain', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=spain_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=spain_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def iran_options():
    clean_frame()

    name = Label(frame_right, text='Iran', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=iran_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=iran_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def usa_options():
    clean_frame()

    name = Label(frame_right, text='USA', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=usa_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=usa_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def japan_options():
    clean_frame()

    name = Label(frame_right, text='Japan', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=japan_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=japan_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def france_options():
    clean_frame()

    name = Label(frame_right, text='France', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=france_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=france_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def germany_options():
    clean_frame()

    name = Label(frame_right, text='Germany', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=germany_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=germany_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def tunisia_options():
    clean_frame()

    name = Label(frame_right, text='Tunisia', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=tunisia_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=tunisia_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def costa_rica_options():
    clean_frame()

    name = Label(frame_right, text='Costa Rica', font=('Arial', 20))
    name.place(relx=0.4, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=costa_rica_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=costa_rica_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def australia_options():
    clean_frame()

    name = Label(frame_right, text='Australia', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=australia_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=australia_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def netherlands_options():
    clean_frame()

    name = Label(frame_right, text='Netherlands', font=('Arial', 20))
    name.place(relx=0.41, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=netherlands_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=netherlands_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def morocco_options():
    clean_frame()

    name = Label(frame_right, text='Morocco', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=morocco_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=morocco_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def serbia_options():
    clean_frame()

    name = Label(frame_right, text='Serbia', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=serbia_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=serbia_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def uruguay_options():
    clean_frame()

    name = Label(frame_right, text='Uruguay', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=uruguay_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=uruguay_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def wales_options():
    clean_frame()

    name = Label(frame_right, text='Wales', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=wales_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=wales_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def south_korea_options():
    clean_frame()

    name = Label(frame_right, text='South Korea', font=('Arial', 20))
    name.place(relx=0.4, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=south_korea_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=south_korea_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def switzerland_options():
    clean_frame()

    name = Label(frame_right, text='Switzerland', font=('Arial', 20))
    name.place(relx=0.4, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=switzerland_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=switzerland_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def denmark_options():
    clean_frame()

    name = Label(frame_right, text='Denmark', font=('Arial', 20))
    name.place(relx=0.43, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=denmark_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=denmark_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def ghana_options():
    clean_frame()

    name = Label(frame_right, text='Ghana', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=ghana_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=ghana_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def ecuador_options():
    clean_frame()

    name = Label(frame_right, text='Ecuador', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=ecuador_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=ecuador_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def canada_options():
    clean_frame()

    name = Label(frame_right, text='Canada', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=canada_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=canada_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def mexico_options():
    clean_frame()

    name = Label(frame_right, text='Mexico', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=mexico_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=mexico_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def cameroon_options():
    clean_frame()

    name = Label(frame_right, text='Cameroon', font=('Arial', 20))
    name.place(relx=0.42, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=cameroon_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=cameroon_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def belgium_options():
    clean_frame()

    name = Label(frame_right, text='Belgium', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=belgium_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=belgium_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def qatar_options():
    clean_frame()

    name = Label(frame_right, text='Qatar', font=('Arial', 20))
    name.place(relx=0.45, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=qatar_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=qatar_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def england_options():
    clean_frame()

    name = Label(frame_right, text='England', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=england_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=england_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def poland_options():
    clean_frame()

    name = Label(frame_right, text='Poland', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=poland_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=poland_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def saudi_arabia_options():
    clean_frame()

    name = Label(frame_right, text='Saudi Arabia', font=('Arial', 20))
    name.place(relx=0.4, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=saudi_arabia_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=saudi_arabia_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def croatia_options():
    clean_frame()

    name = Label(frame_right, text='Croatia', font=('Arial', 20))
    name.place(relx=0.44, rely=0.2)

    matches = ttk.Button(frame_right, text='Matches', command=croatia_matches)
    matches.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.1)

    players = ttk.Button(frame_right, text='Players', command=croatia_players)
    players.place(relx=0.6, rely=0.45, relwidth=0.15, relheight=0.1)


def clean_frame():
    for widget in frame_right.winfo_children():
        widget.destroy()


screen = ThemedTk(theme='black')

screen.title('World Cup 2022')
screen.configure(bg='black')
screen.geometry('900x700')
screen.resizable(True, True)


frame_right = Frame(screen, bd=4)
frame_right.place(relx=0.5, rely=0.02, relwidth=0.48, relheight=0.96)

frame_left = Frame(screen, bd=4)
frame_left.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.96)


brazil = ttk.Button(frame_left, text='Brazil', command=brazil_options)
brazil.place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.05)

portugal = ttk.Button(frame_left, text='Portugal', command=portugal_options)
portugal.place(relx=0.01, rely=0.076, relwidth=0.15, relheight=0.05)

argentina = ttk.Button(frame_left, text='Argentina', command=argentina_options)
argentina.place(relx=0.01, rely=0.15, relwidth=0.15, relheight=0.05)

senegal = ttk.Button(frame_left, text='Senegal', command=senegal_options)
senegal.place(relx=0.01, rely=0.226, relwidth=0.15, relheight=0.05)

spain = ttk.Button(frame_left, text='Spain', command=spain_options)
spain.place(relx=0.01, rely=0.295, relwidth=0.15, relheight=0.05)

iran = ttk.Button(frame_left, text='Iran', command=iran_options)
iran.place(relx=0.01, rely=0.365, relwidth=0.15, relheight=0.05)

usa = ttk.Button(frame_left, text='USA', command=usa_options)
usa.place(relx=0.01, rely=0.435, relwidth=0.15, relheight=0.05)

japan = ttk.Button(frame_left, text='Japan', command=japan_options)
japan.place(relx=0.01, rely=0.505, relwidth=0.15, relheight=0.05)

france = ttk.Button(frame_left, text='France', command=france_options)
france.place(relx=0.01, rely=0.575, relwidth=0.15, relheight=0.05)

germany = ttk.Button(frame_left, text='Germany', command=germany_options)
germany.place(relx=0.01, rely=0.645, relwidth=0.15, relheight=0.05)

tunisia = ttk.Button(frame_left, text='Tunisia', command=tunisia_options)
tunisia.place(relx=0.01, rely=0.715, relwidth=0.15, relheight=0.05)

costa_rica = ttk.Button(frame_left, text='Costa Rica', command=costa_rica_options)
costa_rica.place(relx=0.4, rely=0.01, relwidth=0.15, relheight=0.05)

australia = ttk.Button(frame_left, text='Australia', command=australia_options)
australia.place(relx=0.4, rely=0.076, relwidth=0.15, relheight=0.05)

netherlands = ttk.Button(frame_left, text='Netherlands', command=netherlands_options)
netherlands.place(relx=0.4, rely=0.15, relwidth=0.15, relheight=0.05)

morocco = ttk.Button(frame_left, text='Morocco', command=morocco_options)
morocco.place(relx=0.4, rely=0.226, relwidth=0.15, relheight=0.05)

serbia = ttk.Button(frame_left, text='Serbia', command=serbia_options)
serbia.place(relx=0.4, rely=0.295, relwidth=0.15, relheight=0.05)

uruguay = ttk.Button(frame_left, text='Uruguay', command=uruguay_options)
uruguay.place(relx=0.4, rely=0.365, relwidth=0.15, relheight=0.05)

wales = ttk.Button(frame_left, text='Wales', command=wales_options)
wales.place(relx=0.4, rely=0.435, relwidth=0.15, relheight=0.05)

south_korea = ttk.Button(frame_left, text='South Korea', command=south_korea_options)
south_korea.place(relx=0.4, rely=0.505, relwidth=0.15, relheight=0.05)

switzerland = ttk.Button(frame_left, text='Switzerland', command=switzerland_options)
switzerland.place(relx=0.4, rely=0.575, relwidth=0.15, relheight=0.05)

denmark = ttk.Button(frame_left, text='Denmark', command=denmark_options)
denmark.place(relx=0.4, rely=0.645, relwidth=0.15, relheight=0.05)

ghana = ttk.Button(frame_left, text='Ghana', command=ghana_options)
ghana.place(relx=0.79, rely=0.01, relwidth=0.15, relheight=0.05)

ecuador = ttk.Button(frame_left, text='Ecuador', command=ecuador_options)
ecuador.place(relx=0.79, rely=0.076, relwidth=0.15, relheight=0.05)

canada = ttk.Button(frame_left, text='Canada', command=canada_options)
canada.place(relx=0.79, rely=0.15, relwidth=0.15, relheight=0.05)

mexico = ttk.Button(frame_left, text='Mexico', command=mexico_options)
mexico.place(relx=0.79, rely=0.226, relwidth=0.15, relheight=0.05)

cameroon = ttk.Button(frame_left, text='Cameroon', command=cameroon_options)
cameroon.place(relx=0.79, rely=0.295, relwidth=0.15, relheight=0.05)

belgium = ttk.Button(frame_left, text='Belgium', command=belgium_options)
belgium.place(relx=0.79, rely=0.365, relwidth=0.15, relheight=0.05)

qatar = ttk.Button(frame_left, text='Qatar', command=qatar_options)
qatar.place(relx=0.79, rely=0.435, relwidth=0.15, relheight=0.05)

england = ttk.Button(frame_left, text='England', command=england_options)
england.place(relx=0.79, rely=0.505, relwidth=0.15, relheight=0.05)

poland = ttk.Button(frame_left, text='Poland', command=poland_options)
poland.place(relx=0.79, rely=0.575, relwidth=0.15, relheight=0.05)

saudi_arabia = ttk.Button(frame_left, text='Saudi Arabia', command=saudi_arabia_options)
saudi_arabia.place(relx=0.79, rely=0.645, relwidth=0.15, relheight=0.05)

croatia = ttk.Button(frame_left, text='Croatia', command=croatia_options)
croatia.place(relx=0.79, rely=0.715, relwidth=0.15, relheight=0.05)


screen.mainloop()
