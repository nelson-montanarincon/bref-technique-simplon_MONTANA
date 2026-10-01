import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
print()

#calcul des ventes journaliers en df de pandas
données['CA'] = données['prix'] * données['qte']

#print(données['CA'])

#6.a chiffre d’affaires par produit (CA)
ca_par_produit = (données.groupby('produit')['CA']).sum()
print(f"chiffre d’affaires par  : {ca_par_produit}")
print()


# 6.a.1 la moyenne du CA:
x_ca_par_produit = (données.groupby('produit')['CA']).mean()
print(f"6.a.1 moyenne du CA par  : {x_ca_par_produit}")
print()

# 6.a.2 la médianne du CA:
med_ca_par_produit = (données.groupby('produit')['CA']).median()
print(f"6.a.2 la médianne du CA par  : {med_ca_par_produit}")
print()

# 6.a. volume de ventes par produit (vol)
vol_vt_par_prd = (données.groupby('produit')['qte']).sum()

# 6.a.3 la moyenne du vol_vt_par_produit
x_vol_vt_par_prd = (données.groupby('produit')['qte']).mean()
print(f"6.a.3 la moyenne du volume de ventes par  : {x_vol_vt_par_prd}")
print()

# 6.a.4 la médianne du vol_vt_par_produit
med_vol_vt_par_prd =  (données.groupby('produit')['qte']).median()
print(f"la médianne du volume de ventes par :{med_vol_vt_par_prd}")
print()

#6.b.1 l’écart-type du vol_vt_par_produit
o_vol_vt_par_prd = (données.groupby('produit')['qte']).std()
print(f"6.b.1 l’écart-type du volume de ventes par : {o_vol_vt_par_prd}")
print()

#6.b.2 la variance du vol_vt_par_produit
oo_vol_vt_par_prd = (données.groupby('produit')['qte']).var()
print(f"6.b.2 la variance du volume de ventes par : {oo_vol_vt_par_prd}")
print()

# 7 le produit le plus vendu et le moins vendu en nombre d’unités vendues en Python natif 

pdt_A = 0
pdt_B = 0
pdt_C = 0
pdt_aut = 0

# 7.1 convertir de dataframe en dict
dic_donnees = données.to_dict(orient='records')

# 7.2 looper sur le dict de données
for pdt in dic_donnees:
    produit = pdt['produit']
    qte = pdt['qte']

    if produit == 'Produit A':
        pdt_A = pdt_A + qte
    elif produit == 'Produit B':
        pdt_B = pdt_B + qte
    elif produit == 'Produit C':
        pdt_C = pdt_C + qte
    else: 
        pdt_aut = pdt_aut + qte

# 7.3 creer un dic pour recuperer les valeurs
group = [(pdt_A,'Produit A'), (pdt_B,'Produit B'), (pdt_C,'Produit C')]

# 7.4 fonctions natives de python

print(f"le produit le moins vendu : {min(group)}")
print()
print(f"le produit le plus vendu : {max(group)}")

# 8  créer deux nouveaux graphiques :

#8.a. les ventes par produit :
ca_par_produit_gr3 = (données.groupby('produit')['qte'].sum().reset_index())

fig3 = px.bar(ca_par_produit_gr3, x='qte', y='produit', title='Ventes par produit en unités', orientation='h')


fig3.write_html('8.a.Ventes_unit_par_produit.html')


#8.b. le CA par produit :
ca_par_produit_gr4 = (données.groupby('produit')['CA'].sum().reset_index())

fig4 = px.histogram(ca_par_produit_gr4, x="produit", y="CA", text_auto=True, title='CA par produit')


fig4.write_html('8.b. CA_par_produit.html')

