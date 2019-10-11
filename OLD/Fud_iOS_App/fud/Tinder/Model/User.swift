//
//  User.swift
//  Tinder
//
//  Created by Bekzod Rakhmatov on 26/01/2019.
//  Copyright © 2019 BekzodRakhmatov. All rights reserved.
//

import UIKit

struct User: ProducesCardViewModel {
    
    var name: String?
    var imageUrl1: String?
    var uid: String?

    init(dictionary: [String: Any]) {
        self.name = dictionary["fullName"] as? String ?? ""
        self.imageUrl1 = dictionary["imageUrl1"] as? String
        self.uid = dictionary["uid"] as? String ?? ""
    }
    
    func toCardViewModel() -> CardViewModel {
        
        let attributedText = NSMutableAttributedString(string: name ?? "", attributes: [.font: UIFont.systemFont(ofSize: 32, weight: .heavy)])
    
        var imageUrl = [String]()
        
        /*
        let url = "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/1.png?alt=media&token=4b3ec145-0c43-4fa8-94e7-311e4602815a"
        if let url = imageUrl1 { imageUrls.append(url) }
        url = "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/2.png?alt=media&token=3251e76a-e691-459e-8d57-25472e7f557c"
        if let url = imageUrl2 { imageUrls.append(url) }
        url = "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/3.png?alt=media&token=47e0e18b-4e88-4df0-93e7-a86d6c2dfda7"
        if let url = imageUrl3 { imageUrls.append(url) }
         */
        
        let number = Int.random(in: 0 ..< 3)
        print("random")
        print(number)
        
        let pic = ["https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/1.png?alt=media&token=4b3ec145-0c43-4fa8-94e7-311e4602815a", "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/2.png?alt=media&token=3251e76a-e691-459e-8d57-25472e7f557c",  "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/3.png?alt=media&token=47e0e18b-4e88-4df0-93e7-a86d6c2dfda7",
            "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/4.png?alt=media&token=e2eea8d5-6577-4eaa-83f6-20cf9e2b1eb0",
            "https://firebasestorage.googleapis.com/v0/b/fuud-39473.appspot.com/o/5.png?alt=media&token=ccac1dcc-d066-4c83-89d7-74a16472e056"]
        
        
        let url = pic[number]
        
        imageUrl.append(url)

        print(imageUrl)
        
        return CardViewModel(uid: self.uid ?? "", imageNames: imageUrl, attributedString: attributedText, textAlignment: .left)
    }
}
