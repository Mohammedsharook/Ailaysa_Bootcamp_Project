# Ailaysa Bootcamp Session: 

## Project: SpotGuidance
  SpotGuidance is a platform that helps users discover, share, and rate various spots in different categories. Whether it's a restaurant, a tourist attraction, or a local gym, SpotGuidance allows users to explore spots by category and subcategory, leave reviews and post a comment for spots, and track their favorite or visited places.

--
## Key Features:

#### Categories and Subcategories: 
  - Spots are organized into categories and subcategories, ensuring easy Access.
  
#### Spot Reviews and Ratings: 
  - Users can leave reviews and rate spots to help others make informed decisions.
  
#### User Engagement: 
  - Users can upload their own spots , mark spots as visited or favorite to keep track of places they've been or plan to visit.
  
#### ForumComments: 
  - Engage with other users through the comment system for each spot.

--
## Models Overview:

  ### Category:  
  Represents the top-level grouping of spots (e.g., Food, Health, Education).

    name (CharField): Unique name of the category.
    slug (SlugField): Unique slug for URL-friendly names.
    
### SubCategory:
  Subcategories under each category (e.g., Restaurants under Food).

    name (CharField): Name of the subcategory.
    category (ForeignKey): Associated with the parent category.
    
### Spot:
  Represents individual spots that users can visit or review.

    name (CharField): Name of the spot.
    description (TextField): Detailed description.
    city (CharField): City where the spot is located.
    sub_category (ForeignKey): Linked to a subcategory.
    uploaded_by (ForeignKey): User who uploaded the spot.
    visited_users (ManyToManyField): Users who have visited the spot.
    favorite_users (ManyToManyField): Users who marked the spot as a favorite.

### Review:

  Tracks user reviews and ratings for each spot.

    spot (ForeignKey): Spot being reviewed.
    user (ForeignKey): User who wrote the review.
    rating (IntegerField): Rating from 1 to 5.
    review_text (TextField): Optional text review.
    
### ForumComments:
  Tracks user comments on spots.
--

    message (TextField): The content of the comment.
    posted_by (ForeignKey): User who posted the comment.
    spot (ForeignKey): Spot the comment is related to.
