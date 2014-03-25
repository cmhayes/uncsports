The Roster: UNC Men's Basketball 2012-2013
=========

This is my first Django app. Fully developed and deployed, it would serve as a record of all varsity sports at the University of North Carolina at Chapel Hill. It was completed as an initial class project for J583 Advanced Multimedia at UNC-Chapel Hill. The scope of this project, however, was to focus on the 2012-2013 Men's Basketball team. With that in mind there are three distinct views:

Home
=========
This view holds the landing page for the home site. It presents a carousel of recent news for a variety of UNC sports as well as recent game records and links to each sport's team page.

Team
=========
The team view contains content specific to the selected team. Currently, the page only features the roster with an image of each player that serves as a link to their individual profile page. In the future, one would be able to find season and scouting information.

Player
=========
The third view is dedictaed to displaying brief player bios. This view includes an image of the player, background information and a description of the player's role on the team in previous seasons, if applicable. This view utilizes a JSON file to populate each section of the profile page. In a fully developed version, this page would include game-specific and season statistics for each player. 
