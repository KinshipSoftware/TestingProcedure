 test cases exported from test plan file kinoath_2012-04-04.xml on 2013-11-28 (08:36).

###

###StartKinOath (main testing OS for this version: Mac)

####Webstart
"To start the program go to http://tla.mpi.nl/tools/tla-tools/kinoath > Show all KinOath verions > select the Testing version, and click on 'Run via webstart'. After some seconds KinOath should open."
* Works

####WindowsInstaller
"Before starting to test the program try out the installation on Windows. Go to http://tla.mpi.nl/tools/tla-tools/kinoath/versions/, select the Testing version and the option 'Download the Windows Installer'."
* Works

####LinuxInstaller
"Before starting to test the program try out the installation on Linux. Go to http://tla.mpi.nl/tools/tla-tools/kinoath/versions/, select the Testing version and the option 'Download the Debian Linux Package'. "
* STILL TO BE TESTED

####MacOSInstaller
"Before starting to test the program try out the installation on Mac. Go to http://tla.mpi.nl/tools/tla-tools/kinoath/versions/, select the Testing version and the option 'Download the Mac Installer'.  NOTE: first have a look at  https://trac.mpi.nl/wiki/LATSoftwareTesting, paragraph \"Information for Mac users\"."
* Works

###

###LanguageSelection

###SelectALanguage
"If it is the first time you run the application a window should come out asking you to select the desired language. Choose one then click on OK. KinOath should open in the chosen language."
* Works

###ChangeLanguage
"Try to change the language by selecting 'Select language' in the Help menu. Once you choose one and click on OK you will see a message telling you to quit and restart KinOath for it to apply the language change."
* Works

###SampleDiagramsTest

####FreeformDiagramSyntax1
"From File menu go to 'Open Sample Diagram' and choose 'Freeform Diagram Syntax'. A new page should open with the panel 'Kin Type Strings' on top of it, and the sample diagram in the main panel."
* Works

####FreeformDiagramSyntax2
"From Edit menu choose 'Recalculate the Diagram', or simply click on the central panel. The kin type strings in the top panel should get coloured. Ensure nothing goes missing from the diagram."
* Works

####FreeformDiagramSyntax3
"Try to modify the diagram by adding other kin types (with labels, i.e. names, dates, etc.) to the ones in colour and see if the new entities appear in the diagram."
* Works

####FreeformDiagramSyntax4
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####QueryDiagramSyntax1
"In the File menu go to 'Open Sample Diagram' and choose 'Query Diagram Syntax'. A new page should open showing some sample entities, a left panel with three tabs: 'Search Entities', 'Project Tree', and 'Diagram Tree', and the top panel 'Kin Type Strings'. "
* Works

####QueryDiagramSyntax2
"From Edit menu choose 'Recalculate the Diagram', or simply click on the central panel. You may be requested to import data and the data should import without error. Recalculate again. A diagram should now appear and the kin type strings in the top panel should get coloured. Ensure nothing goes missing from the diagram."
* Works

####QueryDiagramSyntax3
"Select one of the entities on the diagram and try to modify the kinship data in the table at the bottom of the page. The changes should then also appear in the diagram."
* Works

####QueryDiagramSyntax4
"Now insert a random letter in the name of the entity '[Maria Cristina of_Austria]' (at the very beginning of the 'Kin type strings' panel). An error message should pop up telling you to import the 'European Royalty' sample data. Do the import (not necessary if import has already been performed). Once it is complete you should see, on the right of the page, a panel called 'Imported Entities'. (Delete the lettere inserted before moving on)"
* Works

####QueryDiagramSyntax5
"Try a query in the 'Kin Type Strings', like for example x[Albert]. In the central panel you should see all the entities named Albert. (Then delete the query before moving on.)"
* Works

####QueryDiagramSyntax6
"Now select one entity in the 'Imported Entities' panel. It should appear in the main panel. Then check the option 'Expand selection by kin type string' and try different strings (e.g. P, C, *, etc.). New entities related to the one you had previously selected should appear/disappear accordingly."
* Works

####HawaiianKinTerms1
"In the File menu go to 'Open Sample Diagram' and choose 'Hawaiian Kin Terms'. A new page should open with the diagram in the centre and a panel on the right called 'Hawaiian Kin Terms'."
* Works

####HawaiianKinTerms2
"Choose 'Recalculate the Diagram' from 'Edit' menu, or simply click on the central panel. Now check the option 'Show Kin Types Labels' in the 'Diagram Options' menu. The kin type strings should become visible in the diagram."
* Works

####HawaiianKinTerms3
"Try to modify the diagram by adding other information (kin terms, kin type strings, descriptions) in the table in the right panel (it doesn't matter in which language). The new individuals should appear in the diagram. "
* Works

####HawaiianKinTerms3b
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####HawaiianKinTerms4
"Uncheck 'Show On Graph' in the right panel: the kin terms on the diagram should go away."
* Works

####HawaiianKinTerms5
"From 'Kin Terms' menu choose 'New Kin Term Group'. A new tab should open in the right panel. Choose a color for the new group and add kin terms, kin type strings, descriptions. The latter should appear in the diagram in the previously chosen colour."
* Works

####HawaiianKinTerms6
"In the 'Hawaiian Kin Terms' tab in the right panel check some of the kin terms and select 'Delete Selected' on the top of the table. Those kin terms should disappear from the table and from the diagram."
* Works

####HawaiianKinTerms6b
"Now try the option 'Delete Group'. The kin terms group should disappear both from the tab on the right of page ad from the diagram in the main panel."
* Kind of works: the group is only deleted from the Kin Terms tab on the right of the page, but it is still present on the diagram. Reference issue #274.

####HawaiianKinTerms7
"Try to uncheck the option 'Generate Example Entities' in the panel on the right (it should be checked by default). The diagram should disappear.  NOTE: if you have two kin terms groups, and some of the kin terms overlap, these will not disappear unless you select the option for both groups."
* Works

####JapaneseKinTerms1
"In the File menu go to 'Open Sample Diagram' and choose 'Japanese Kin Terms'. A new page should open with the diagram in the centre, the top panel 'Kin Type Strings', and two kin terms groups on the right ('Japanese Kin Terms(Vocative)' and 'Japanese Kin Terms(Referential)')."
* Works

####JapaneseKinTerms2
"Choose 'Recalculate the Diagram' from 'Edit' menu, or simply click on the central panel. Try to modify the diagram by adding other information (kin terms, kin type strings, descriptions) in the table in the right panel (it doesn't matter in which language). The new individuals should appear in the diagram. Do it for both groups: Vocative and Referential."
* Works

####JapaneseKinTerms3
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####JapaneseKinTerms4
"Uncheck 'Show On Graph' in the right panel for both groups: the kin terms on the diagram should go away."
* Works

####JapaneseKinTerms5
"From 'Kin Terms' menu choose 'New Kin Term Group'. A new tab should open in the right panel. Choose a color for the new group and add individuals. The latter should appear in the diagram in the previously chosen colour."
* Works

####JapaneseKinTerms5b
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####JapaneseKinTerms6
"In the table in the right panel check some of the kin terms and select 'Delete Selected' on the top of the table. Those kin terms should disappear from the table and from the diagram"
* Works

####JapaneseKinTerms6b
"Now try the option 'Delete Group'. The kin terms group should disappear both from the tab on the right of page ad from the diagram in the main panel."
* Kind of works: the group is only deleted from the Kin Terms tab on the right of the page, but it is still present on the diagram. Reference issue #274.

####JapaneseKinTerms7
"Try to uncheck the option 'Generate Example Entities' in the panel on the right (it should be checked by default). Do it for all the kin terms groups. The diagram should disappear. NOTE: if you have two kin terms groups, and some of the kin terms overlap, these will not disappear unless you select the option for both groups.  "
* Works

####SwedishKinTerms1
"In the File menu go to 'Open Sample Diagram' and choose 'Swedish Kin Terms'. A new page should open with the diagram in the centre and a panel on the right called 'Swedish Kin Terms'. Check the option 'Show Kin Types Labels' in the 'Diagram Options' menu. The kin type strings should become visible in the diagram."
* Works

####SwedishKinTerms2
"Choose 'Recalculate the Diagram' from Edit menu, or simply click on the central panel. Try to modify the diagram by adding other information (kin terms, kin type strings, descriptions) in the table in the right panel (it doesn't matter in which language). The new individuals should appear in the diagram."
* Works

####SwedishKinTerms3
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####SwedishKinTerms4
"Uncheck 'Show On Graph' in the right panel: the kin terms on the diagram should go away."
* Works

####SwedishKinTerms5
"From 'Kin Terms' menu choose 'New Kin Term Group'. A new tab should open in the right panel. Choose a color for the new group and add individuals. The latter should appear in the diagram in the previously chosen colour."
* Works

####SwedishKinTerms5b
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####SwedishKinTerms6
"In the table in the right panel check some of the kin terms and select 'Delete Selected' on the top of the table. Those kin terms should disappear from the table and from the diagram"
* Works

####SwedishKinTerms6b
"Now try the option 'Delete Group'. The kin terms group should disappear both from the tab on the right of page ad from the diagram in the main panel."
* Kind of works: the group is only deleted from the Kin Terms tab on the right of the page, but it is still present on the diagram. Reference issue #274.

####SwedishKinTerms7
"Try to uncheck the option 'Generate Example Entities' in the panel on the right (it should be checked by default). The diagram should disappear.  NOTE: if you have two kin terms groups, and some of the kin terms overlap, these will not disappear unless you select the option for both groups."
* Works

####NamedTransientEntities1
"In the File menu go to 'Open Sample Diagram' and choose 'Named Transient Entities'. A new page should open with a small diagram in the centre and the top panel 'Kin Type Strings'."
* Works

####NamedTransientEntities2
"From Edit menu choose 'Recalculate the Diagram', or simply click on the central panel. The kin type strings in the top panel should get coloured. Ensure nothing goes missing from the diagram."
* Works

####NamedTransientEntities3
"Check the option 'Show Kin Types Labels' in the 'Diagram Options' menu. The kin type strings should become visible in the diagram. Now try to modify the diagram by adding other kin types (with labels, i.e. names, dates, etc.) to the ones in colour and see if the new entities appear in the diagram."
* Works

####NamedTransientEntities4
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####MatrimonialRingsExamples1
"In the File menu go to 'Open Sample Diagram' and choose 'Matrimonial Rings Examples'. A new page should open with some diagrams in the centre and the top panel 'Kin Type Strings'."
* Works

####MatrimonialRingsExamples2
"In the Edit menu choose 'Recalculate the Diagram'. The kin type strings in the top panel should get coloured. Ensure nothing goes missing from the diagram."
* Works

####CharlesIIOfSpain1
"In the File menu go to 'Open Sample Diagram' and choose 'Charles II of Spain'. A new page should open with the diagram in the centre and the top panel 'Kin Type Strings'. "
* Works

####CharlesIIOfSpain2
"In the Edit menu choose 'Recalculate the Diagram'. The kin type strings in the top panel should get coloured. Ensure nothing goes missing from the diagram."
* Works

####CharlesIIOfSpain3
"Check the option 'Show Kin Types Labels' in the 'Diagram Options' menu. The kin type strings should become visible in the diagram.Then try to modify the diagram by adding other kin types (with labels, i.e. names, dates, etc.) to the ones in colour and see if the new entities appear in the diagram. "
* Works

####CharlesIIOfSpain4
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####HaemophiliaEu1
"In the File menu go to 'Open Sample Diagram' and choose 'Haemophilia in European Royalty'. A new page should open with the part of the diagram in the centre, a left panel with three tabs: 'Search Entities', 'Project Tree', and 'Diagram Tree', and the top panel 'Kin Type Strings'. "
* Works

####HaemophiliaEu2
"From Edit menu choose 'Recalculate the Diagram', or simply click on the central panel. The kin type strings in the top panel should get coloured. Ensure nothing goes missing from the diagram. You may also be asked to import the sample data. "
* Works

####HaemophiliaEu3
"Now insert a random letter in the name of the entity '[Maria Cristina of_Austria]' (at the very beginning of the 'Kin type strings' panel). An error message should pop up telling you to import the 'European Royalty' sample data. Do the import (not necessary if import has already been performed). Once it is complete you should see, on the right of the page, a panel called 'Imported Entities'. (Delete the inserted letter before following with the next task.) "
* Works

####HaemophiliaEu4
"Try a query in the 'Kin Type Strings', like for example x[Albert]. In the central panel you should see all the entities named Albert. (Delete the query before moving on)"
* Works

####HaemophiliaEu5
"Now select one entity in the 'Imported Entities' panel. It should appear in the main panel. Then check the option 'Expand selection by kin type string' and try different strings (e.g. P, C, *, etc.). New entities related to the one you had previously selected should appear/disappear accordingly."
* Works

####HaemophiliaEu6
"Select one of the entities from the sample diagram and try to modify its kinship data (bottom table). The changes should then appear also in the diagram."
* Works

###

###NewDiagramsTest "Once you have created new diagrams leave them open so that you can use them for the 'Menus' testing (see below)."

####StandardDiagram1
"In the File menu go to 'New Diagram of Type' and select 'Standard Diagram (current project)'. A new page should open with a central, blank panel and a panel on the left with three tabs: 'Diagram Tree', 'Project Tree', 'Search Entities'."
* Works

####StandardDiagram2
"Start creating a small diagram by adding individuals with a right click > 'Add' > 'Individual'. After creating an entity select it and fill in the table at the bottom (name of the entity, gender, etc). Then save the information by clicking on the entity in the diagram. "
* Works

####StandardDiagram3
"In the table at the bottom also enter some dates and then check 'Show Date Labels' from the 'Diagram Options' menu. The dates should appear in the diagram next to the entities. Uncheck it and they should go away."
* Works

####StandardDiagram4
"Create relations between the individuals by selecting two or more (hold the SHIFT button while selecting), right click, 'Add relation', choose the type of relation. The entities should be linked accordingly. "
* Works

####StandardDiagram4b
"Try to add relations in a different way, i.e. by using the blue dots that come out when selecting an entity. Starting from the top they stand for: ancestor, sibling, union, descendant."
* Works

####StandardDiagram5
"Remove the previously created relation by selecting the two individuals, right click, 'Remove Relations' > 'Remove relations between selected'. The link bewteen the two should go away."
* Works (although a number of tickets is related to the issue of relations removal: #248, #262, #266, #267)

####ChromosomeType
"Right click in the main panel, select 'Add' > 'Chromosome_Example'. This should create a new entity. Fill in again the table at the bottom adding also the chromosome type (if it's an entity affected by haemophilia, i.e. with Xx or xY chrom. type, a red spot will appear next to the shape)."
* Works

####ClanExample
"Right click in the main panel, select 'Add' > 'Clan_Example'. This should create a new entity. Fill in some of the information in the table at the bottom of the page. Click on the entity to save the information entered. Some of them should now appear next to entity on the diagram."
* Works

####KinTerm
"Right click in the main panel, select 'Add' > 'KinTerm'. You should get a different icon. Select it and fill in some of the information in the table at the bottom of the page. Click on the entity to save the information entered. Some of them should now appear next to entity on the diagram."
* Works

####SocialEvent
"Right click in the main panel, select 'Add' > 'Social_Event'. Select the entity and fill in some of the information in the table at the bottom of the page. Click on the entity to save the information entered. Some of them should now appear next to entity on the diagram."
* Works

####Geometry1
"Right click in the main panel, 'Add Geometry' > 'Add Label'. The word 'Label' should appear in the central panel. Click on it. In the window at the bottom of the page write something; then click again on the word 'Label' in the main panel: there should appear what you wrote."
* Works

####Geometry2
"Right click in the main panel, 'Add Geometry'. Try to select the various options, circle, square, etc. The forms should appear in the mail panel."
* Works

####Delete
"After creating an entity, select it, right click, choose 'Delete selected from project'. A dialog window should open warning you that the entity selected will be deleted from the database."
* Works

####Merge
"Select two entities that you want to merge into one single individual. Right click, choose 'Merge Selected Entities'. Now you should see only one individual carrying the labels of both merged entities. "
* Works

####Duplicate
"Select an entity, right click, choose 'Duplicate Selected Entities'. Another entity carrying the same labels should appear.  "
* Works

####SetEgo
"Select one entity, right click, 'Set as Ego (list will be cleared)'. If you look at the \"diagram tree\" tab on the left of the page the entity selected should appear under the 'Attached' list and go black."
* Works

####AddEgoList
"Select another entity, right click, 'Add to ego list'. This entity should now also appear in 'Attached' in the \"diagram tree\" tab and go black."
* Works

####RemoveEgoList
"Select one of the egos. Right click, 'Remove from ego list'. The entity should remain in the 'Attached' list and go white again."
* Works

####AttachToDiagram
"Import some data. From the panel 'Imported Entities' select an entity. According to the kin type string entered (P, C, *, etc) you will see a diagram forming into the main panel. Now select one entity on the diagram. Right click. 'Attach to diagram'. In the Diagram Tree tab you should see the entity moving from Search Results to Attached."
* Works

####Release
"Select one entity, right click, 'Release from diagram'. The entity should disappear from the diagram and from the \"diagram tree\" tab (but not from the database as with 'Delete')."
* Works

####ResetZoom
"With the mouse cursor in the diagram window right click and then choose 'Reset zoom'. The diagram should go back to its default size."
* Works

####ResetLayout
"With the mouse cursor in the diagram window right click and choose 'Reset layout'. The entities' position should change."
* Works

####SaveChanges
"Select one entity, in the table at the bottom of the page change some of the information. Click on the diagram, the new information should be saved."
* Works

####StandardDiagram6
"Open the 'Search Entities' tab on the left and enter the name of an individual present in the database; click 'Search'; the list of entities found should appear in the same panel. Click on some of them, they should appear in the diagram. NOTE: if you want more than one entity to appear in the main panel you have to drag them. "
* Works

####StandardDiagram6b
"Try also the options 'Graph selection' [uncheck it: the entity you select from the 'Project Tree' tab needs to be dragged to the main panel] and 'Expand selection by kin type string' [see Query Diagram Syntax above]. "
* Works

####FreeformDiagram1
"In the File menu go to 'New Diagram of Type' and select 'Freeform Diagram (transient)'. A new page should open with a central, blank panel, and a 'Kin Type Strings' panel above it. "
* Works

####FreeformDiagram2
"Create a diagram by entering kin type strings in the suitable panel. The new individuals should appear in the diagram. "
* Works

####FreeformDiagram3
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####KinTerms1
"In the File menu go to 'New Diagram of Type' and select 'Kin Terms Diagram (transient)'. A new page should open with a central, blank panel and, on the right, a 'Kin Term Group' panel."
* Works

####KinTerms2
"Enter some kin terms, plus the corresponding kin type strings and descriptions in the table in the right panel. The new entities should appear in the central panel in a new diagram. "
* Works

####KinTerms2b
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####KinTerms3
"Uncheck 'Show On Graph' in the right panel: the kin terms on the diagram should go away."
* Works

####KinTerms4
"From 'Kin Terms' menu choose 'New Kin Term Group'. A new tab should open in the right panel. Choose a color for the new group and add individuals. The latter should appear in the diagram in the previously chosen colour."
* Works

####KinTerms4b
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####KinTerms5
"In the table in the right panel check some of the kin terms and select 'Delete Selected' on the top of the table. Those kin terms should disappear from the table and from the diagram."
* Works

####KinTerms5b
"Now try the option 'Delete Group'. The kin terms group should disappear both from the tab on the right of page ad from the diagram in the main panel."
* Kind of works: : the group is only deleted from the Kin Terms tab on the right of the page, but it is still present on the diagram. Reference issue #274.

####KinTerms6
"Try to uncheck the option 'Generate Example Entities' in the panel on the right (it should be checked by default). Do it for both kin terms groups. The diagram should disappear.  NOTE: if you have two kin terms groups, and some of the kin terms overlap, these will not disappear unless you select the option for both groups."
* Works

####QueryDiagram1
"In the File menu go to 'New Diagram of Type' and select 'Query Diagram (current project)'. A new page should open with a central, blank panel, a 'Kin Type Strings' panel on the top, and a panel on the left with two tabs: 'Diagram Tree' and 'Project Tree'."
* Works

####QueryDiagram2
"Try a query by searching an entity present in the database, like for example f[Antonia]. Both in the central panel and in the diagram tree tab you should see all the entities found named Antonia."
* Works

####QueryDiagram3
"From the diagram tree tab take one of the entities found and drag it next to your first query f[Antonia] to make it more specific. Now in the central panel (and also in the diagram tree panel) you should see  only one entity named Antonia. In the diagram tree panel - by clicking on the little arrow on the left of the entity - you should see also the number of entities related to the one searched and the corresponding relation types."
* Works

####ArchiveLinker1 (from here the test is done on a Windows machine)
"From File menu go to New Diagram of Type and then Archive Data Linker. A new page should open with a central, blank panel, a panel on the left with two tabs (Project and Diagram Tree), and a panel on the right with a tab called Archive Linker. The latter should display the IMDI tree. (You may see two tabs more, both called Archive Linker, but with different sections of the tree)"
* Works

####ArchiveLinker2
"Choose a node where you see actors (e.g. MPI corpora > Demo > DOBES training > PeWi corpus). Drag them to the main panel. They should carry labels like \"archive ref.: 1,2, etc\", and such links should also be visible in a table at the bottom of the page, in the tab \"External Links\""
* Doesn't work: there are no "archive ref." labels, but only the name of the node (e.g. Actors (4)), and also, the data in the "External Link" tab at the bottom of the page disappear once you have selected something else in the diagram/main panel.

####ArchiveLinker3
"Try to create some entities and then random relations between the entities."
* Works

####ArchiveLinker4
"Now take a resource from the tree (you can follow the path indicated in test no. 41). First drag it to the diagram: it should create another entity. Then drag it to an entity in the diagram tree: it should create another link to the entity. "
* Works (in this case I can see the "archive ref." label)

###

###Menus

####SaveFile
"Take one of the diagrams you created. Choose 'Save as (...)' and - after naming it - save the file. "
* Works

####OpenDiagram
"From the File menu go to 'Open Diagram'. A new window should appear with all the documents you can open. Choose the one you saved in the previous test and 'Open'. Then try to recalculate it. "
* Works

####RecentDiagram
"From the File menu go to 'Open recent diagram' and select one from the list. "
* Works

####RecentDiagram2
"Go again to 'Open recent diagram', but this time select 'clear list': all the diagrams which were in the list should disappear.  "
* Works

####NewProject
"From the File menu choose New Project. Give it a name and a directory and click on Save. Now on top of the open KinOath page you should see the name of the project."
* Works

####NewProject2
"Create a small diagram. "
* Works

####ProjectDefault
"From File menu select 'Set Project Default Diagram as (...)'. Close and re-open the application."
* Works

####OpenProject
"From the File menu choose Open Project. Choose the project you have just set as default and click on Open. The project should open showing the diagram in the main panel."
* Works

####OpenRecentProject
"From the File menu choose Open Recent Project and select one among those present in the list. It should again appear in the main panel. Try to recalculate the diagram."
* Works

####ClearList
"From the File menu choose Open Recent Project and then 'clear list'. It should delete the list of projects recently opened."
* Works

####Gedcom_CSV
"From the File menu go to 'Import Gedcom/CSV/TIP File'. A window should appear with the documents you can open. Choose one (NOT .ged) and click on 'Open'. The import window should open, and once the import has finished you should see the panel 'Imported Entities' on the right of the page.  "
* TO BE TESTED

####GedcomResources
"From the File menu go to 'Import Gedcom/CSV/TIP File'. A window should appear with the documents you can open. Choose a .ged file and click on 'Open'. (If it is not possible to locate a .ged file in this way, highlight Import Sample Data from the File Menu and choose the Gedcom Torture File from the dropdown menu which appears.) The import window should open, and once the import has finished another 'Imported Entities' tab should open on the right of the page.."
* Works

####GedcomResources2
"Select an entity from the 'Imported Entities' panel (select those containing external links, such as 'Extra URL/Filelinks/). This should appear in the main panel carrying a label like: \"archive ref.: 1, 2, ...\""
* Works

####ExportPDF
"Take one of the diagrams you created. Choose 'Export as PDF/JPEG/PNG/TIFF' from the File menu. A window should open asking you to choose a directory, a file name, and a file format. Choose PDF. After saving check if it has been effectively exported in the chosen format. "
* Works

####ExportJPEG
"Take one of the diagrams you created. Choose 'Export as PDF/JPEG/PNG/TIFF' from the File menu. A window should open asking you to choose a directory, a file name, and a file format. Choose JPEG. After saving check if it has been effectively exported in the chosen format. "
* Works

####ExportPNG
"Take one of the diagrams you created. Choose 'Export as PDF/JPEG/PNG/TIFF' from the File menu. A window should open asking you to choose a directory, a file name, and a file format. Choose PNG. After saving check if it has been effectively exported in the chosen format. "
* Works

####ExportTIFF
"Take one of the diagrams you created. Choose 'Export as PDF/JPEG/PNG/TIFF' from the File menu. A window should open asking you to choose a directory, a file name, and a file format. Choose TIFF. After saving check if it has been effectively exported in the chosen format. "
* Works

####ExportR_SPSS
"Take one of the diagrams you created. Choose 'Export for R / SPSS' from the File menu. A window should open asking you to choose a directory and a file name. Then save. Check in the directory if it has been exported correctly. The format should be .tab."
* Works

####Close
"From the File menu choose 'Close (...)'. Only the page you are working on should close."
* Works

####GlobalDefaultDiagram
"Choose a diagram type (File menu > New Diagram of Type). Then, from File menu, select 'Set Global Default Diagram as (...)'. Close and re-open the application: it should show the diagram type page you set as default."
* Works

####NewDefaultDiagram
"After setting the default diagram choose - from the File menu - 'New (default diagram)'. It should open a new page with the diagram previously set. "
* Works

####Edit
"Take the standard diagram you created before, recalculate it in the 'Edit' menu, then check whether the various options of the 'Edit' menu work (they should highlight partially or completely the lines connecting the entities, or serve to modify the diagram). "
* Works

####DiagramOptions
"Take the standard diagram you created before and try to uncheck and check again the various options of the 'Diagram Options' menu to see if changes effectively occur. For the options 'Show Kin Type Labels' and 'Show Id Labels' use the freeform diagram. "
* Works

####Settings
"From the menu 'DiagramOptions' select Settings. A dialog window should appear, with some sub-tabs."
* Works

####EntityProfiles
"Choose the tab 'Entity Profiles': some of the profiles of the list should be checked, and should appear when you right click in the main panel to add entities."
* Works

####KinTypeDefinitions
"Choose the tab 'Kin Type Definitions'. Add a new kin type to the list. Then from 'Panels' menu choose 'Kin Type Strings'. This should open on top of the page."
* Works

####KinTypeDefinitions2
"Make a query by taking one of the entities present in the panel on the left and drag it to the 'Kin Type Strings' panel, preceded by the 'x' of 'undefined ego' and followed by the new kin type you added. The required entities should appear in the main panel."
* I am not sure whether this option is working correctly or not. After making the query and dragging the entity to the Kin Type Strings panel nothing happens to the diagram, not even after adding the new kin type.

####LabelFields
"Choose the tab 'Label Fields'. Delete the info included in the panel on the top (small square on the right). The labels of the entity should go away. From the drop-down menu in the table choose the entity labels you want (e.g. name, date of birth, of death, etc.) and click on Add. The information should be back next to the entity. "
* Works

####SymbolFields
"Choose the 'Symbol Fields'. Try to modify the shapes corresponding to the kin terms and types, by choosing from the drop down menus. They should change also in the diagram."
* Works

####RelationTypeDefinitions
"Choose the tab 'Relation Type Definitions'. It should contain a table with 7 possible columns to fill in."
* Works

####CustomName
"In the first column, \"Custom Name\", enter a possible name for the relation. If you choose 'other' as relation type, by default the custom name should be 'undefined' but try to modify it."
* Works

####DataCategory
"Enter the following link: http://www.isocat.org/datcat/DC-3688. Then click on it. It should redirect you to the corresponding ISOcat webpage."
* Works

####RelationType
"Choose the type of relation from the drop down menu, or select (on the right of the page) 'Scan For Types': it should find all the relation types present in the diagram and place them automatically in the column"
* Works

####LineColour
"For each relation type choose a different color. Depending on whether you used the \"Scan For Types\" option, either the lines in the diagram get the chosen color automatically, or you will have to use the colored dots."
* Works

####LineWidth
"Change the width of the lines and check if they effectively get thicker or thinner."
* Works

####LineDash
"Change the size of the dashes building up the lines."
* Works

####LineOrientation
"As relation type choose other and then try the two options: horizontal and vertical. The line linking the entities should change position. NOTE: this option is NOT valid for sanguine lines, so create another entity separate from the diagram."
* Works

####DeleteSelected
"Check one or more of the relations and select 'Delete Selected'. The corresponding lines should not be coloured anymore."
* Works

####KinTerms
"Take the kin terms diagram you created before (or create a new one) and from the menu 'Kin Terms' select 'New Kin Term Group'. A panel should open on the right of the page. Choose a color for the new group and add individuals. The latter should appear in the diagram."
* Works

####KinTerms2
"Check also if, once you have added new entities or labels, the layout is correct or if it modifies wrongly."
* Works (although when you add several entities to an already somewhat crowded diagram these are placed in strange locations)

####Export
"Take the kin terms diagram you created before and select 'Export' from the menu 'Kin Terms' on the top. A window should open asking you to choose a directory and to give the file a name. Check in the directory if it has effectively been exported (it should be a .csv file)."
* Works

####Import
"Now re-open one of the kin terms sample diagrams and, from the menu 'Kin Terms' select 'Import'. In the window that will open choose the file you previously saved. Another window should open saying that a certain number of kin terms has been imported and these should be seen in the diagram."
* Kind of works: only the entities of one group have been imported (and probably also exported then?)

####ArchiveLinker
"Open a new page. From Panels menu select the item 'Archive Linker'. On the right of the page you should see a tab called 'The TLA Language Archive' (plus, possibly, 'Arbil Remote Corpus' and 'Arbil Local Corpus')."
* Works

####ArchiveLinker2
"Select an entity from the project tree on the left and drag it to the central panel. Now select a media file from the TLA tab (you can follow the path indicated in test group no.3, test no. 41), and drag it to the previously selected entity in the diagram tree. It should now carry the label 'archive ref: 1'."
* Works

####ArchiveLinker3
"Select the entity on the diagram carrying the archive reference. In the kinship data table at the bottom of the page you should see the tab 'External Links', with some data about the media files attached. "
* Works

####Panels
"This menu should contain all the possible panels that you can open. Take the standard diagram you created before (or open a new standard diagram page), check and/or uncheck the options available and see if the panels effectively appear and/or disappear on the page. NOTE: EXPORT DATA PANEL IS NOT IMPLEMENTED YET. IT WILL HAVE TO BE TESTED FOR NEXT VERSIONS."
* Works

####Plugins
"Select this menu. You should see the possibly open plugins. If there are none, you should see <no plugins found>."
* Works

####Window
"This menu should list all the windows that have been opened. Each window should have the corresponding diagram/panel checked."
* Works

####Help
"Check if the links to manual, website, etc. work"
* Works

####Exit
"From the File menu go to 'Exit'. It should close all the KinOath pages that were previously opened."
* Works

###

###Other_Platforms

####Different_OS_Install
"Install KinOath on other platforms, different from the one you used for the testing. Open KinOath."
* Works
* Kind of works
* Doesn't work

####Opening_Diagram
"In the File menu select 'Open Sample Diagram', then 'Haemophilia in European Royalty'. A new page should open with a central panel showing parts of the diagram, a 'Kin Type Strings' panel on top, and a panel on the left with three tabs: 'Diagram Tree', 'Project Tree', and 'Search Entities'. "
* Works
* Kind of works
* Doesn't work

####Recalculate_Diagram
"From Edit menu select \"Recalculate the diagram\". The entities in the Kin Type Strings panel should get coloured. (You may have to import data first. Do the import)"
* Works
* Kind of works
* Doesn't work

####Import_Data
"Insert a random letter in the name of the entity '[Maria Cristina of_Austria]' (at the very beginning of the 'Kin type strings' panel). An error message should appear prompting one to import 'European Royalty' sample data. Import data (DON'T if you have already imported for the previous test). Once completed, a panel called 'Imported Entities' should be visible to the right of the screen. (Remember to delete inserted letter before proceeding.) "
* Works
* Kind of works
* Doesn't work

####Query
"Make a query in the 'Kin Type Strings' panel by typing for x[Albert], for example. In the central panel all the entities named Albert should now be visible. (Remember to delete your query before moving on)"
* Works
* Kind of works
* Doesn't work

####Select_and_Expand
"Select an entity in the 'Imported Entities' panel. It should appear in the main panel. Then check 'Expand selection by kin type string' and specify different strings (e.g. P, C, *) in the field above the list in the imported entities panel. New entities related to the one previously selected should appear/disappear accordingly."
* Works
* Kind of works
* Doesn't work

####Modify_Kinship_Data
"Select one of the entities from the sample diagram and try to modify its kinship data (bottom table). These changes ought to be reflected in the diagram."
* Works
* Kind of works
* Doesn't work

###

###DropboxTest "Before starting this part of the test, make sure Dropbox is installed on your machine."

####NewProject
"From File menu choose New Project. Save it into the Dropbox folder."
* Works
* Kind of works
* Doesn't work

####Diagram
"Create a (standard) diagram, and then set it as Project Default Diagram (from File menu)."
* Works
* Kind of works
* Doesn't work

####DifferentMachine
"Go to another computer and open the project you have just created (open it from the Dropbox folder!). An updating message should come out. Recalculate the diagram. NOTE: if you have set your project as default, when you re-open on the other machine it you will see it in the central panel. If you haven't, you will only see the entities under the Project Tree on the left."
* Works
* Kind of works
* Doesn't work

####ModifyDiagram
"Try to modify the diagram and save the changes. Close the application again."
* Works
* Kind of works
* Doesn't work

####Reindexing
"Go back to the computer where you initially created the project. Open the project again. A message should appear saying that your project has been modified externally and asking to reindex the files. Do the reindexing."
* Works
* Kind of works
* Doesn't work

####Reindexing2
"Modify again the diagram. Save the changes. Go to the other computer and try the reindexing there as well."
* Works
* Kind of works
* Doesn't work

