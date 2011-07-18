### About
pySNP was created to help me learn python and support [Snarl](http://www.fullphat.net/) at the same time. It communicates with Snarl via [SNP 2.0](http://sourceforge.net/apps/mediawiki/snarlwin/index.php?title=SNP_2.0_API).

### Actions:
* **snRegister**
  * app-sig _(Required)_
  * title _(Required)_
  * icon _(Optional)_
  * password _(Optional)_
* **snNotify**
  * app-sig _(Required)_
  * title _(Required)_
  * text _(Required)_
  * icon _(Optional)_
  * password _(Optional)_
  * id _(Optional)_
  * uid _(Optional)_
  * timeout _(Optional)_
  * priority _(Optional)_
* **snAddClass**
  * app-sig _(Required)_
  * id _(Required)_
  * name _(Required)_
  * title _(Optional)_
  * text _(Optional)_
  * icon _(Optional)_
  * password _(Optional)_
  * enabled _(Optional)_
* **snVersion**
* **snUnregister**
  * app-sig _(Required)_
  * password _(Optional)_

### How to use:
Start by importing pySNP.

Example:

    import pySNP
    snarl = pySNP.pySNP()

Anything in the list above that is marked _"Required"_, the value of it can go directly inside quotations inside the function call. They NEED to be in the order listed above.

Example:

    snarl.pySNP.snRegister('requiredSIG', 'requiredTITLE')

Anything in the list above that is marked _"Optional"_, the value of it goes after the paramater and equal (=) sign in quoatations.

Example:

    snarl.pySNP.snRegister('requiredSIG', 'requiredTITLE', password='optionalPASS', icon='optionalICON')

### TODO:
* add more actions
* additional tweaks to make it better
