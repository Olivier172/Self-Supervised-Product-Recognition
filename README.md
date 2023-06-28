# Self-Supervised Product Recognition
Welcome to the repository of my Master's thesis! 

## Abstract [EN]
Self-supervised learning methods are closing the gap with supervised pre-training methods. 
With this paradigm it is possible to pre-train models on large unlabeled datasets, avoiding the costly operation of manually annotating. After this pre-training step, the model is a trained feature extractor. 
In this thesis we will mainly look at two approaches of doing this self-supervised pre-training: pretext task based and using contrastive learning. 
We will test the capabilities of different models by comparing the produced embeddings in features space. 
By query matching a feature representation to a set of pre-computed labeled embeddings in an embedding gallery, we can test how well these representation vectors from different classes can be distinguished. 
We find that performance of SSL models is already significant in this early stage without any supervised training. 
The next step is to fine-tune a classifier on top of the learned features with a limited amount of labeled examples. 
We will investigate whether we can deploy Self-Supervised Learning (SSL) models to ultimately classify different supermarket products. 
We find that state-of-the-art (SOTA) SSL models such as Rotnet, Jigsaw, MoCo and SimCLR perform well in this setting. 
Their performance is put into perspective in comparison to randomly initialized weights and ImageNet pre-trained weights (as a target to approach or surpass). 
We find that contrastive learning methods perform best, especially the MoCo model pre-trained with a batch size of 64 achieving mAP scores of up to 79.4%.
We observe that Self-supervised pre-training can provide value in our use case of classifying everyday products from the grocery store. 
All code implementations for this thesis can be found here.

## Abstract [NL]
Self-supervised learning-methoden dichten de kloof met supervised pre-training-methoden. 
Met dit paradigma is het mogelijk om modellen te pre-trainen op grote ongannoteerde datasets, waarbij de kostbare opdracht van het handmatig annoteren wordt vermeden. 
Na deze pre-training stap is het model een getrainde feature extractor. 
In deze thesis zullen we hoofdzakelijk twee benaderingen bekijken om deze self-supervised pre-training uit te voeren: pretext task based en met behulp van contrastive learning. 
We zullen de mogelijkheden van de verschillende modellen testen door de geproduceerde embeddings in de feature space te vergelijken. 
Door query matching van een feature representation aan een reeks vooraf berekende gelabelde embeddings in een embedding gallery, kunnen we testen hoe goed deze representations van verschillende klassen kunnen worden onderscheiden. 
Wij stellen vast dat de prestaties van SSL modellen al in dit vroege stadium aanzienlijk zijn zonder enige gesuperviseerde training. 
De volgende stap is het verfijnen van een classifier bovenop de geleerde feature representations met een beperkte hoeveelheid gelabelde voorbeelden. 
We zullen onderzoeken of we Self-Supervised Learning (SSL) modellen kunnen inzetten om uiteindelijk verschillende supermarktproducten te classificeren. 
We vinden dat state-of-the-art (SOTA) SSL modellen zoals Rotnet, Jigsaw, MoCo en SimCLR goed presteren in deze setting. 
Hun prestaties worden in perspectief geplaatst in vergelijking met willekeurig ge ̈ınitialiseerde gewichten en ImageNet voorgetrainde gewichten (met als doel om deze te benaderen of te overtreffen). 
Er werd vastgesteld dat contrastive learning methoden het best presteren, vooral het MoCo model dat vooraf is getraind met een batch size van 64, waarmee mAP scores tot 79, 4% worden behaald. 
Wij constateren dat self-supervised pre-training waardevol kan zijn in ons geval van classificatie van alledaagse producten uit de supermarkt. 
Alle code-implementaties voor deze thesis zijn hier te vinden.

## Additional explanation

### Pre-processing
In the folder "pre-processing" you can find the `imagecrop.py` program that crops out the SKU110K dataset.
It saves these crops in a training, test and validation set for SSL pre-training.

### Pre-training
In the folder "pretraining" you can find all yaml configuration files that I used for pre-training with VISSL.
For more information about how to execute SSL pre-training, I recommend taking a look at the [VISSL documentation](https://vissl.readthedocs.io/en/v0.1.6/).

### Evaluation and fine-tuning
In the folder "evaluation_and_finetuning" you can find all the scripts I used for:
- Creating the embedding galleries (`embedding_gallery.py`, `load_vissl_model.py`)
- evaluating embedding quality (`similarity_matrix.py`)
- fine-tuning and evaluating classifiers (`cross_validation.py`, `performance_assessment.py`)
- logging and plotting results for the thesis (`log_processing.py`)

The program `query_origin.py` is used to determine the strict train-test split.

### Testing notebooks and extras
The folder testing notebooks contains some of the notebooks I used for testing purposes before making a computationally heavy script.
The folder extras contains some extra scripts I used for creating figures and extracting data for the thesis.


 

