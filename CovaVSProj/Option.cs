//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CovaVSProj
{
    using System;
    using System.Collections.ObjectModel;
    
    public partial class Option
    {
        public int id { get; set; }
        public int security_id { get; set; }
        public int underlyer_id { get; set; }
        public int expiry_date_id { get; set; }
        public string strike { get; set; }
        public Nullable<int> open_interest { get; set; }
    
        public virtual ExpiryDate ExpiryDate { get; set; }
        public virtual Security Security { get; set; }
        public virtual Security Security1 { get; set; }
    }
}
