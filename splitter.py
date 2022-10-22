import splitfolders

splitfolders.ratio("classes", # The location of dataset
                   output="div", # The output location
                   seed=42, # The number of seed
                   ratio=(.8, .2), # The ratio of splited dataset
                 
                   )

