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
    
    public partial class Watchlist
    {
        public int id { get; set; }
        public int member_map_id { get; set; }
        public string name { get; set; }
    
        public virtual MemberMap MemberMap { get; set; }
    }
}
