# TLDR

This folder holds the Make.com automation blueprints for automating the distribution
of user generated images to Instagram & X.com. The interface for interacting with this scenario
is a Google Spreadsheet and a Google Drive.

## Requirements

- an X.com account
- an Instagram account
- a Gmail account
- a Make.com

## Schema of Google Spreadsheet

Post Type |	Prompt | Image Link | ImageLinkID | Timestamp | Processed

```txt
Post Type - Image + Text
Prompt - User defined
Image Link - https://drive.google.com/file/d/18vT3GzjtE2NdiuOiccHxfejVdN3zeBRk/view?usp=sharing
ImageLinkID - 18vT3GzjtE2NdiuOiccHxfejVdN3zeBRk
Timestamp - 1/30/2025
Processed - TRUE | FALSE
```