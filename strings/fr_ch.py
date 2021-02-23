# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Part of the translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "CHF"

# Positioning of the currency symbol
currency_format_string = "{value} {symbol}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} disponible"

# Copies of a product in cart
in_cart_format_string = "{quantity} dans le panier"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Commande #{id}"

# Order info string, shown to the admins
order_format_string = "par {user}\n" \
                      "Créée le {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAL: <b>{value}</b>\n" \
                      "\n" \
                      "Note du client: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Commande {status_text}</b>\n" \
                           "{items}\n" \
                           "TOTAL: <b>{value}</b>\n" \
                           "\n" \
                           "Note: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Chargement des transactions...\n" \
                       "Veuillez patienter quelques secondes.</i>"

# Transactions page
transactions_page = "Page <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Un fichier 📄 .csv contenant toutes les transactions stockées dans la base de données du chatbot a été généré.\n" \
              "Vous pouvez ouvrir ce fichier avec d'autres programmes, tels que LibreOffice Calc ou Microsoft Excel ou Apple Numbers, pour traiter" \
              " les données."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Bonjour !\n" \
                           "Bienvenue sur greed!\n" \
                           "Ceci est une version 🅱️ <b>Beta</b> du logiciel.\n" \
                           "Il est entièrement utilisable, mais il se peut que certains bugs soient encore présents.\n" \
                           "Si vous en trouvez, veuillez les signaler à https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Que voulez-vous faire ?\n" \
                              "💰 Vous avez <b>{credit}</b> dans votre porte-monnaie.\n" \
                              "\n" \
                              "<i>Appuyer sur une touche du clavier du bas pour sélectionner une opération.\n" \
                              "Si le clavier ne s'est pas ouvert, vous pouvez l'ouvrir en appuyant sur le bouton avec quatre petits" \
                              " carrés dans la barre de message.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Vous être un 💼 <b>Gestionnaire</b> de ce magasin !\n" \
                               "Que voulez-vous faire ?\n" \
                               "\n" \
                               "<i>Appuyer sur une touche du clavier du bas pour sélectionner une opération.\n" \
                               "Si le clavier ne s'est pas ouvert, vous pouvez l'ouvrir en appuyant sur le bouton avec quatre petits" \
                               " carrés dans la barre de message.</i>"

# Conversation: select a payment method
conversation_payment_method = "Comment voulez-vous ajouter des fonds à votre porte-monnaie ?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Quel produit voulez-vous mettre à jour?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Quel produit voulez-vous effacer?"

# Conversation: select a user to edit
conversation_admin_select_user = "Sélectionnez un utilisateur pour le mettre à jour."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Ajouter des produits au panier en faisant défiler vers le haut et en appuyant sur le bouton Ajouter au dessous" \
                            " des produits que vous souhaitez ajouter au panier. Lorsque vous avez terminé, revenez à ce message et" \
                            " appuyez sur le bouton Terminer ci-dessous.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Votre panier contient les produits suivants:\n" \
                            "{product_list}" \
                            "Total: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Si vous voulez continuer, appuyez sur le bouton Terminer en dessous de ce message.\n" \
                            "Pour annuler, appuyez sur le bouton Annuler.</i>"

# Live orders mode: start
conversation_live_orders_start = "You are in <b>Live Orders</b> mode\n" \
                                 "Toutes les nouvelles commandes passées par les clients apparaîtront en temps réel dans ce chat, et vous" \
                                 " pourrez les marquer comme ✅ Complétées" \
                                 " ou ✴️ Rembourser le crédit au client."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Appuyer sur le bouton Stop ci-dessous pour arrêter la" \
                                " diffusion.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "De quel type d'aide avez-vous besoin ?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Êtes-vous sûr de vouloir promouvoir cet utilisateur comme 💼 Gestionnaire ?\n" \
                                       "C'est une action irréversible !"

# Conversation: language select menu header
conversation_language_select = "Choisissez une langue :"

# Conversation: switching to user mode
conversation_switch_to_user_mode = "Vous passez en mode client 👤.\n" \
                                   "Si vous voulez retourner au menu du Gestionnaire 💼, relancez la conversation avec /start."

# Notification: the conversation has expired
conversation_expired = "🕐 Je n'ai reçu aucun message depuis un certain temps, alors j'ai fermé la conversation pour sauvegarder" \
                       " ressources.\n" \
                       "Si vous voulez en démarrer un nouveau, envoyez une nouvelle commande /start."

# User menu: order
menu_order = "🛒 Commander des produits"

# User menu: order status
menu_order_status = "🛍 Mes commandes"

# User menu: add credit
menu_add_credit = "💵 Ajouter des fonds"

# User menu: bot info
menu_bot_info = "ℹ️ Information du chatbot"

# User menu: cash
menu_cash = "💵 Avec de l'argent liquide"

# User menu: credit card
menu_credit_card = "💳 Par carte de crédit"

# Admin menu: products
menu_products = "📝️ Produits"

# Admin menu: orders
menu_orders = "📦 Commandes"

# Menu: transactions
menu_transactions = "💳 Liste des transactions"

# Menu: edit credit
menu_edit_credit = "💰 Créer une transaction"

# Admin menu: go to user mode
menu_user_mode = "👤 Passez en mode client"

# Admin menu: add product
menu_add_product = "✨ Nouveau produit"

# Admin menu: delete product
menu_delete_product = "❌ Supprimer un produit"

# Menu: cancel
menu_cancel = "🔙 Annuler"

# Menu: skip
menu_skip = "⏭ Passer"

# Menu: done
menu_done = "✅️ Terminer"

# Menu: pay invoice
menu_pay = "💳 Payer"

# Menu: complete
menu_complete = "✅ Complet"

# Menu: refund
menu_refund = "✴️ Remboursement"

# Menu: stop
menu_stop = "🛑 Stop"

# Menu: add to cart
menu_add_to_cart = "➕ Ajouter"

# Menu: remove from cart
menu_remove_from_cart = "➖ Enlever"

# Menu: help menu
menu_help = "❓ Aide / Support"

# Menu: guide
menu_guide = "📖 Guide"

# Menu: next page
menu_next = "▶️ Suivant"

# Menu: previous page
menu_previous = "◀️ Précédent"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contacter le magasin"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Editer les Gestionnaires"

# Menu: language
menu_language = "🇨🇭 Langue"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "en attente"

# Text: completed order
text_completed = "complété"

# Text: refunded order
text_refunded = "remboursé"

# Add product: name?
ask_product_name = "Quel doit être le nom du produit ?"

# Add product: description?
ask_product_description = "Quelle doit être la description du produit ?"

# Add product: price?
ask_product_price = "Quel doit être le prix du produit ?\n" \
                    "Entrez <code>X</code> si vous ne voulez pas que le produit soit encore en vente."

# Add product: image?
ask_product_image = "🖼 Quelle image voulez-vous que le produit ait ?\n" \
                    "\n" \
                    "<i>Envoyer la photo, ou Passer cette phase et ne pas ajouter d'image.</i>"

# Order product: notes?
ask_order_notes = "Voulez-vous laisser une note avec la commande ?\n" \
                  "💼 Elle sera visible par les Gestionnaires du magasin.\n" \
                  "\n" \
                  "<i>Envoyer un message avec la note que vous voulez laisser, ou appuyer sur le bouton Passer en dessous du" \
                  " message pour ne rien laisser.</i>"

# Refund product: reason?
ask_refund_reason = "Joindre une raison à ce remboursement.\n" \
                    "👤  Elle sera visible pour le client."

# Edit credit: notes?
ask_transaction_notes = "Attacher une note à cette transaction.\n" \
                        "👤 Elle sera visible par le client après le crédit / débit" \
                        " et aux 💼 Gestionnaires dans le journal des transactions."

# Edit credit: amount?
ask_credit = "Comment voulez-vous modifier le crédit du client ?\n" \
             "\n" \
             "<i>Envoyer un message contenant le montant.\n" \
             "Utilisez le signe </i><code>+</code><i> pour ajouter du crédit sur le compte du client," \
             " et le signe </i><code>-</code><i> pour le déduire.</i>"

# Header for the edit admin message
admin_properties = "<b>Permissions de {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Mettre à jour les produits"

# Edit admin: can receive orders?
prop_receive_orders = "Recevoir des commandes"

# Edit admin: can create transactions?
prop_create_transactions = "Gérer les transactions"

# Edit admin: show on help message?
prop_display_on_help = "Afficher au client"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Je télécharge votre photo !\n" \
                    "Cela pourrait prendre un certain temps... S'il vous plaît, soyez patients !\n" \
                    "Je ne pourrai pas vous répondre pendant le téléchargement."

# Edit product: current value
edit_current_value = "La valeur actuelle est :\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Appuyez sur le bouton Passer en dessous de ce message pour garder la même valeur.</i>"

# Payment: cash payment info
payment_cash = "Vous pouvez payer en espèces à l'emplacement physique du magasin.\n" \
               "Payez à la caisse, et donnez ce numéro au gérant :\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "Combien de fonds voulez-vous ajouter à votre porte-monnaie?\n" \
                    "\n" \
                    "<i>Sélectionnez un montant avec les boutons ci-dessous, ou saisissez-le manuellement avec le clavier normal</i>"

# Payment: add funds invoice title
payment_invoice_title = "Ajout de fonds"

# Payment: add funds invoice description
payment_invoice_description = "Le paiement de cette facture ajoutera {amount} à votre porte-monnaie."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Recharger"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Frais de transaction"

# Notification: order has been placed
notification_order_placed = "Une nouvelle commande a été passée :\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Votre commande a été complétée !\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Votre commande a été remboursée !\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Une nouvelle transaction a été appliquée à votre porte-monnaie :\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Motif du remboursement :\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Ce chatbot utilise <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' un framework par @Steffo pour les paiements avec Telegram, publié dans le cadre de la' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Help: guide
help_msg = "le guide de greed's est disponible à cette adresse :\n" \
           "https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/"

# Help: contact shopkeeper
contact_shopkeeper = "Actuellement, le personnel disponible pour fournir une assistance aux utilisateurs est composé de :\n" \
                     "{shopkeepers}\n" \
                     "<i>Cliquez / Touchez l'un de leurs noms pour les contacter dans un chat Telegram.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Le produit a été ajouté/modifié avec succès !"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Le produit a été supprimé avec succès !"

# Success: order has been created
success_order_created = "✅ La commande a été envoyée avec succès !\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Vous avez marqué la commande #{order_id} comme terminée."

# Success: order was refunded successfully
success_order_refunded = "✴️ La commande #{order_id} a été remboursée."

# Success: transaction was created successfully
success_transaction_created = "✅ La transaction a été créée avec succès!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Ce bot ne fonctionne que dans les chats privés."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ La conversation avec le chatbot a été interrompue.\n" \
                           "Pour la redémarrer, envoyez la commande /start au bot."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 La conversation avec le chatbot commence actuellement.\n" \
                         "S'il vous plaît, attendez quelques instants avant d'envoyer d'autres commandes !"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Le montant maximum qui peut être ajouté en une seule transaction est {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Le montant minimum qui peut être ajouté en une seule transaction est {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Cette facture a expiré et a été annulée. Si vous voulez toujours ajouter des fonds, utilisez le menu" \
                        " Ajouter des fonds."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Un produit portant le même nom existe déjà."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ Vous n'avez pas assez de crédit pour passer la commande."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Cette commande a déjà été traitée."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  Vous n'avez pas encore passé de commande, il n'y a donc rien à afficher."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  L'utilisateur sélectionné n'existe pas."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh non ! Une <b>erreur</b> a interrompu cette conversation\n" \
                               "L'erreur a été signalée au propriétaire du chatbot afin qu'il puisse la corriger..\n" \
                               "Pour relancer la conversation, envoyez à nouveau la commande /start."

