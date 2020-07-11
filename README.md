# RoofN3D_Classification_MVCNNSA
To run the train code:
python controller.py 'Path for the Views' --model resnet_att --depth 18 -p 100 -b 32 -- epochs 1000 

To run the test code:
python controller.py 'Path for the Views' --model resnet_att --depth 18 -p 100 -b 32 -- epochs 1000 -r 'Path to checkpoint folder'
