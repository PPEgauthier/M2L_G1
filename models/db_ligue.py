# -*- coding: utf-8 -*-
db.define_table('ligue',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('adresseRue','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('cp','string',requires=IS_NOT_EMPTY()),
             Field('tel','string',requires=IS_NOT_EMPTY()),
             Field('URLSiteWeb','string'),
             Field('emailContact','string')  
             ,migrate=False
               )

db.define_table('adherent',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('prenom','string',requires=IS_NOT_EMPTY()),
             Field('dateNaissance','string',requires=IS_NOT_EMPTY()),
             Field('sexe','string',requires=IS_NOT_EMPTY()),
             Field('adresseRue','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('cp','string',requires=IS_NOT_EMPTY()),
             Field('numLicence','string',requires=IS_NOT_EMPTY()),
             Field('tel','string',requires=IS_NOT_EMPTY()),
             Field('email','string')
             ,Field('idLigue','reference ligue',requires=IS_IN_DB(db,db.ligue.id))
             ,migrate=True,fake_migrate=True
               )

db.define_table('formation',
             Field('libelle','string',requires=IS_NOT_EMPTY()),
             Field('dateDeb','datetime',requires=IS_DATETIME()),
             Field('dateFin','datetime',requires=IS_DATETIME()),
             Field('nbPlaces','string',requires=IS_NOT_EMPTY()),
             Field('dateEcheance','datetime',requires=IS_DATETIME())
             ,migrate=True,fake_migrate=True
                )

db.define_table('inscription',
             #Field('numLicence','reference licence',requires=IS_IN_DB(db.db.licence.id)),
             Field('idFormation','reference formation',requires=IS_IN_DB(db,db.formation.id)),
             Field('idAdherent','reference adherent',requires=IS_IN_DB(db,db.adherent.id)),
             Field('dateInscription','datetime',requires=IS_DATETIME()),
             Field('situationActuelle','string',requires=IS_NOT_EMPTY()),
             Field('association','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('discipline','string',requires=IS_NOT_EMPTY()),
             Field('dateDebutAdherent','datetime',requires=IS_DATETIME()),
             Field('titulairePSC1','string',requires=IS_NOT_EMPTY()),
             Field('activiteBenevole','string',requires=IS_NOT_EMPTY()),
             Field('libelleActiviteBenevole','string',requires=IS_NOT_EMPTY()),
             Field('commentaireFormation','string',requires=IS_NOT_EMPTY()),
             Field('autreAssociation','string',requires=IS_NOT_EMPTY()),
             migrate=True, fake_migrate=True
                )
